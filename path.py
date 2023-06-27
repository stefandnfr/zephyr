import sys, os

with open("TF-CMakeLists.txt", "w", encoding="utf-8") as out:

    header = '''
# Copyright (c) 2021 Intel Corporation
# Copyright 2022 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: Apache-2.0

if(CONFIG_TENSORFLOW_LITE_MICRO)

set(TENSORFLOW_LITE_MICRO_DIR ${ZEPHYR_CURRENT_MODULE_DIR})

zephyr_library()


# include these directories
zephyr_include_directories(
${TENSORFLOW_LITE_MICRO_DIR}/../../hal/nxp/mcux/mcux-sdk/CMSIS/NN/
${TENSORFLOW_LITE_MICRO_DIR}/../../hal/nxp/mcux/mcux-sdk/CMSIS/
${TENSORFLOW_LITE_MICRO_DIR}/../../hal/nxp/mcux/mcux-sdk/CMSIS/DSP/Include/
)

zephyr_include_directories(
    ${TENSORFLOW_LITE_MICRO_DIR}/.
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party/flatbuffers/include
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party/hexagon
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party/ruy
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party/gemmlowp
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party_static/flatbuffers/include
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party/ruy
)

if(CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)
    set(CMSIS_NN_OPTIMIZED_KERNEL_DIR cmsis_nn)
    set(tflm_cmsis_nn_glue_path ${ZEPHYR_CMSIS_MODULE_DIR})

    zephyr_library_include_directories(${tflm_cmsis_nn_glue_path})
    zephyr_library_compile_definitions(CMSIS_NN)
endif()


zephyr_library_sources(
'''



    out.write(header)


    search_dir = "./tflite-micro/tensorflow"
    root = "./tflite-micro"
    extension = (".cc",".c")

    excludes = ["ethosu","flatbuffer_size","riscv32","tflite_flatbuffer_align_wrapper","chre","benchmarks","examples","hexagon","experimental","xtensa","ceva", "arc","test","cmsis", "cortex_m","unidirectional_sequence_lstm","lstm_eval_common","bluepill"]

    for r, d, f in os.walk(search_dir):
        for file in f:
            if file.endswith(extension):
                skip = False

                p = os.path.join(r, file)
                relative_path = os.path.relpath(p,root)



                for ex in excludes:
                    if ex in relative_path:
                        skip = True
                if skip:
                    continue
                print(relative_path)

                line = "\t" + "${TENSORFLOW_LITE_MICRO_DIR}/" + relative_path + "\n"

                out.write(line)
    out.write('''
  )

endif()''')