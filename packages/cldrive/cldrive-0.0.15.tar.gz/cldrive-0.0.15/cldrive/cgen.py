# Copyright (C) 2017 Chris Cummins.
#
# This file is part of cldrive.
#
# Cldrive is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Cldrive is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cldrive.  If not, see <http://www.gnu.org/licenses/>.
#
import numpy as np

import cldrive
from cldrive import *


def escape_c_string(s: str) -> str:
    """ quote and return the given string """
    return '\n'.join('"{}\\n"'.format(line.replace('"','\\"'))
                     for line in s.split('\n') if len(line.strip()))


def to_array_str(array):
    if array.dtype == np.dtype("bool"):
        stringify = lambda x: "1" if x else "0"
    else:
        stringify = repr

    array_values = ', '.join(stringify(x) for x in array.tolist())
    return f"{{ {array_values} }}"


def gen_data_blocks(args: List[KernelArg], inputs: np.array):
    setup_c, teardown_c, print_c = [], [], []
    for i, (arg, array) in enumerate(zip(args, inputs)):
        ctype = cldrive.args.OPENCL_TYPES[array.dtype]
        # we don't support printing all types:
        format_specifier = cldrive.args.FORMAT_SPECIFIERS.get(array.dtype, None)

        if arg.is_pointer:
            array_str = to_array_str(array)

            flags = "CL_MEM_COPY_HOST_PTR"
            if arg.is_const:
                flags += " | CL_MEM_READ_ONLY"
            else:
                flags += " | CL_MEM_READ_WRITE"

            setup_c.append(f"""\
    {ctype} host_{i}[{array.size}] = {array_str};
    cl_mem dev_{i} = clCreateBuffer(ctx, {flags}, sizeof({ctype}) * {array.size}, &host_{i}, &err);
    check_error("clCreateBuffer", err);
    err = clSetKernelArg(kernel, {i}, sizeof(cl_mem), &dev_{i});
    check_error("clSetKernelArg", err);
""")
            if format_specifier and not arg.is_const:
                teardown_c.append(f"""\
    err = clEnqueueReadBuffer(queue, dev_{i}, CL_TRUE, 0, sizeof({ctype}) * {array.size}, &host_{i}, 0, NULL, NULL);
    check_error("clEnqueueReadBuffer", err);
""")
                print_c.append(f"""\
    printf("{arg}:");
    for (int i = 0; i < {array.size}; i++) {{
        printf(" {format_specifier}", host_{i}[i]);
    }}
    printf("\\n");
""")
        else:
            if array.size > 1:
                data_val = to_array_str(array)
                setup_c.append(f"{ctype} host_{i}[{array.size}] = {data_val};")
            else:
                setup_c.append(f"{ctype} host_{i} = {array[0]};")

            setup_c.append(f"""\
    err = clSetKernelArg(kernel, {i}, sizeof({ctype}), &host_{i});
    check_error("clSetKernelArg", err);
""")

    return (
        '\n'.join(setup_c).rstrip(),
        '\n'.join(teardown_c).rstrip(),
        '\n'.join(print_c).rstrip()
    )


def emit_c(env: OpenCLEnvironment, src: str, inputs: np.array,
           gsize: NDRange, lsize: NDRange, timeout: int=-1,
           optimizations: bool=True, profiling: bool=False,
           debug: bool=False, compile_only: bool=False,
           create_kernel: bool=True) -> np.array:
    """
    Generate C code to drive kernel.

    Parameters
    ----------
    env : OpenCLEnvironment
        The OpenCL environment to run the kernel in.
    src : str
        The OpenCL kernel source.
    inputs : np.array
        The input data to the kernel.
    optimizations : bool, optional
        Whether to enable or disbale OpenCL compiler optimizations.
    profiling : bool, optional
        If true, print OpenCLevent times for data transfers and kernel
        executions to stderr.
    timeout : int, optional
        Cancel execution if it has not completed after this many seconds.
        A value <= 0 means never time out.
    debug : bool, optional
        If true, silence the OpenCL compiler.
    compile_only: bool, optional
        If true, generate code only to compile the kernel, not to generate
        inputs and run it.
    create_kernel: bool, optional
        If 'compile_only' parameter is set, this parameter determines whether
        to create a kernel object after compilation. This requires a kernel
        name.

    Returns
    -------
    str
        Code which can be compiled using a C compiler to drive the kernel.

    Raises
    ------
    ValueError
        If input types are incorrect.
    TypeError
        If an input is of an incorrect type.
    LogicError
        If the input types do not match OpenCL kernel types.
    PorcelainError
        If the OpenCL subprocess exits with non-zero return  code.
    RuntimeError
        If OpenCL program fails to build or run.

    Examples
    --------
    TODO
    """
    src_string = escape_c_string(src)
    optimizations_on_off = "on" if optimizations else "off"

    clBuildProgram_opts = "NULL" if optimizations else '"-cl-opt-disable"'

    ids = env.ids()
    c = f"""
/*
 * Usage: gcc -DPLATFORM_ID=0 -DDEVICE_ID=0 code.c -lOpenCL; ./a.out
 *
 * Code generated using cldrive <https://github.com/ChrisCummins/cldrive>
 */
#ifndef PLATFORM_ID
# define PLATFORM_ID {ids[0]}
#endif

#ifndef DEVICE_ID
# define DEVICE_ID {ids[1]}
#endif

#include <stdio.h>
#include <stdlib.h>

#ifdef __APPLE__
#include <OpenCL/opencl.h>
#else
#include <CL/cl.h>
#endif

#define True 1
#define False 0
typedef unsigned char bool;
typedef unsigned short ushort;

const char *kernel_src = \\
{src_string};

const char *clerror_string(cl_int err) {{
    /* written by @Selmar http://stackoverflow.com/a/24336429 */
    switch(err) {{
        /* run-time and JIT compiler errors */
        case 0: return "CL_SUCCESS";
        case -1: return "CL_DEVICE_NOT_FOUND";
        case -2: return "CL_DEVICE_NOT_AVAILABLE";
        case -3: return "CL_COMPILER_NOT_AVAILABLE";
        case -4: return "CL_MEM_OBJECT_ALLOCATION_FAILURE";
        case -5: return "CL_OUT_OF_RESOURCES";
        case -6: return "CL_OUT_OF_HOST_MEMORY";
        case -7: return "CL_PROFILING_INFO_NOT_AVAILABLE";
        case -8: return "CL_MEM_COPY_OVERLAP";
        case -9: return "CL_IMAGE_FORMAT_MISMATCH";
        case -10: return "CL_IMAGE_FORMAT_NOT_SUPPORTED";
        case -11: return "CL_BUILD_PROGRAM_FAILURE";
        case -12: return "CL_MAP_FAILURE";
        case -13: return "CL_MISALIGNED_SUB_BUFFER_OFFSET";
        case -14: return "CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST";
        case -15: return "CL_COMPILE_PROGRAM_FAILURE";
        case -16: return "CL_LINKER_NOT_AVAILABLE";
        case -17: return "CL_LINK_PROGRAM_FAILURE";
        case -18: return "CL_DEVICE_PARTITION_FAILED";
        case -19: return "CL_KERNEL_ARG_INFO_NOT_AVAILABLE";

        /* compile-time errors */
        case -30: return "CL_INVALID_VALUE";
        case -31: return "CL_INVALID_DEVICE_TYPE";
        case -32: return "CL_INVALID_PLATFORM";
        case -33: return "CL_INVALID_DEVICE";
        case -34: return "CL_INVALID_CONTEXT";
        case -35: return "CL_INVALID_QUEUE_PROPERTIES";
        case -36: return "CL_INVALID_COMMAND_QUEUE";
        case -37: return "CL_INVALID_HOST_PTR";
        case -38: return "CL_INVALID_MEM_OBJECT";
        case -39: return "CL_INVALID_IMAGE_FORMAT_DESCRIPTOR";
        case -40: return "CL_INVALID_IMAGE_SIZE";
        case -41: return "CL_INVALID_SAMPLER";
        case -42: return "CL_INVALID_BINARY";
        case -43: return "CL_INVALID_BUILD_OPTIONS";
        case -44: return "CL_INVALID_PROGRAM";
        case -45: return "CL_INVALID_PROGRAM_EXECUTABLE";
        case -46: return "CL_INVALID_KERNEL_NAME";
        case -47: return "CL_INVALID_KERNEL_DEFINITION";
        case -48: return "CL_INVALID_KERNEL";
        case -49: return "CL_INVALID_ARG_INDEX";
        case -50: return "CL_INVALID_ARG_VALUE";
        case -51: return "CL_INVALID_ARG_SIZE";
        case -52: return "CL_INVALID_KERNEL_ARGS";
        case -53: return "CL_INVALID_WORK_DIMENSION";
        case -54: return "CL_INVALID_WORK_GROUP_SIZE";
        case -55: return "CL_INVALID_WORK_ITEM_SIZE";
        case -56: return "CL_INVALID_GLOBAL_OFFSET";
        case -57: return "CL_INVALID_EVENT_WAIT_LIST";
        case -58: return "CL_INVALID_EVENT";
        case -59: return "CL_INVALID_OPERATION";
        case -60: return "CL_INVALID_GL_OBJECT";
        case -61: return "CL_INVALID_BUFFER_SIZE";
        case -62: return "CL_INVALID_MIP_LEVEL";
        case -63: return "CL_INVALID_GLOBAL_WORK_SIZE";
        case -64: return "CL_INVALID_PROPERTY";
        case -65: return "CL_INVALID_IMAGE_DESCRIPTOR";
        case -66: return "CL_INVALID_COMPILER_OPTIONS";
        case -67: return "CL_INVALID_LINKER_OPTIONS";
        case -68: return "CL_INVALID_DEVICE_PARTITION_COUNT";

        /* extension errors */
        case -1000: return "CL_INVALID_GL_SHAREGROUP_REFERENCE_KHR";
        case -1001: return "CL_PLATFORM_NOT_FOUND_KHR";
        case -1002: return "CL_INVALID_D3D10_DEVICE_KHR";
        case -1003: return "CL_INVALID_D3D10_RESOURCE_KHR";
        case -1004: return "CL_D3D10_RESOURCE_ALREADY_ACQUIRED_KHR";
        case -1005: return "CL_D3D10_RESOURCE_NOT_ACQUIRED_KHR";

        default: return "Unknown OpenCL error";
    }}
}}

void check_error(const char* api_call, cl_int err) {{
    if(err != CL_SUCCESS) {{
        fprintf(stderr, "%s %s\\n", api_call, clerror_string(err));
        exit(1);
    }}
}}

int main() {{
    int err;

    cl_uint num_platforms;
    cl_platform_id *platform_ids = (cl_platform_id*)malloc(sizeof(cl_platform_id) * (PLATFORM_ID + 1));
    err = clGetPlatformIDs(PLATFORM_ID + 1, platform_ids, &num_platforms);
    check_error("clGetPlatformIDs", err);

    if (num_platforms <= PLATFORM_ID) {{
        fprintf(stderr, "Platform ID %d not found\\n", PLATFORM_ID);
        return 1;
    }}
    cl_platform_id platform_id = platform_ids[PLATFORM_ID];

    char strbuf[256];
    err = clGetPlatformInfo(platform_id, CL_PLATFORM_NAME, sizeof(strbuf), strbuf, NULL);
    check_error("clGetPlatformInfo", err);
    fprintf(stderr, "[cldrive] Platform: %s\\n", strbuf);

    cl_uint num_devices;
    cl_device_id *device_ids = (cl_device_id*)malloc(sizeof(cl_device_id) * (DEVICE_ID + 1));
    err = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_ALL, DEVICE_ID + 1, device_ids, &num_devices);
    check_error("clGetDeviceIDs", err);

    if (num_devices <= DEVICE_ID) {{
        fprintf(stderr, "Device ID %d not found\\n", DEVICE_ID);
        return 1;
    }}
    cl_device_id device_id = device_ids[DEVICE_ID];

    err = clGetDeviceInfo(device_id, CL_DEVICE_NAME, sizeof(strbuf), strbuf, NULL);
    check_error("clGetDeviceInfo", err);
    fprintf(stderr, "[cldrive] Device: %s\\n", strbuf);

    cl_context ctx = clCreateContext(NULL, 1, &device_id, NULL, NULL, &err);
    check_error("clCreateContext", err);

    cl_command_queue queue = clCreateCommandQueue(ctx, device_id, 0, &err);
    check_error("clCreateCommandQueue", err);

    fprintf(stderr, "[cldrive] OpenCL optimizations: {optimizations_on_off}\\n");

    cl_program program = clCreateProgramWithSource(ctx, 1, (const char **) &kernel_src, NULL, &err);
    check_error("clCreateProgramWithSource", err);

    int build_err = clBuildProgram(program, 0, NULL, {clBuildProgram_opts}, NULL, NULL);

    size_t log_size;
    err = clGetProgramBuildInfo(program, device_id, CL_PROGRAM_BUILD_LOG, 0, NULL, &log_size);
    check_error("clGetProgramBuildInfo", err);

    if (log_size > 2) {{
        char* log = (char*)malloc(sizeof(char) * (log_size + 1));
        err = clGetProgramBuildInfo(program, device_id, CL_PROGRAM_BUILD_LOG, log_size, log, NULL);
        check_error("clGetProgramBuildInfo", err);
        fprintf(stderr, "%s", log);
    }}

    check_error("clBuildProgram", build_err);
    """

    if not compile_only or (compile_only and create_kernel):
        kernel_name_ = kernel_name(src)
        c += f"""
    fprintf(stderr, "[cldrive] Kernel: \\\"{kernel_name_}\\\"\\n");
    cl_kernel kernel = clCreateKernel(program, "{kernel_name_}", &err);
    check_error("clCreateKernel", err);
"""

    if not compile_only:
        args = extract_args(src)
        setup_block, teardown_block, print_block = gen_data_blocks(args, inputs)
        c += f"""
{setup_block}

    const size_t lsize[3] = {{ {lsize.x}, {lsize.y}, {lsize.z} }};
    const size_t gsize[3] = {{ {gsize.x}, {gsize.y}, {gsize.z} }};

    err = clEnqueueNDRangeKernel(queue, kernel, 3, NULL, gsize, lsize, 0, NULL, NULL);
    check_error("clEnqueueNDRangeKernel", err);

{teardown_block}

    err = clFinish(queue);
    check_error("clFinish", err);

{print_block}

    /* clReleaseMemObject(); */
    clReleaseProgram(program);
    clReleaseKernel(kernel);
    clReleaseCommandQueue(queue);
    clReleaseContext(ctx);
"""

    # close out main():
    c += f"""
    fprintf(stderr, "done.\\n");
    return 0;
}}
"""
    return c
