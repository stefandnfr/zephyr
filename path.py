import sys, os

with open("TF-CMakeLists.txt", "w", encoding="utf-8") as out:

    header = '''
# Copyright (c) 2021 Intel Corporation
# Copyright 2022 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: Apache-2.0
if(CONFIG_TENSORFLOW_LITE_MICRO)

set(TENSORFLOW_LITE_MICRO_DIR ${ZEPHYR_CURRENT_MODULE_DIR})

zephyr_library()

zephyr_include_directories(
    ${TENSORFLOW_LITE_MICRO_DIR}/.
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party_static/gemmlowp
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party_static/flatbuffers/include
    ${TENSORFLOW_LITE_MICRO_DIR}/third_party_static/ruy
)

if(CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)
    set(CMSIS_NN_OPTIMIZED_KERNEL_DIR cmsis_nn)
    set(tflm_cmsis_nn_glue_path ${ZEPHYR_CMSIS_MODULE_DIR})

    zephyr_library_include_directories(${tflm_cmsis_nn_glue_path})
    zephyr_library_compile_definitions(CMSIS_NN)
endif()

if (CONFIG_ARM_ETHOS_U)
    set(ETHOSU_CO_PROCESSOR ethos_u)
endif()

zephyr_library_sources(
'''



    out.write(header)


    search_dir = "./modules/lib/tflite-micro/tensorflow"
    root = "./modules/lib/tflite-micro"
    extension = (".cc",".c")
    for r, d, f in os.walk(search_dir):
        for file in f:
            if file.endswith(extension):
                p = os.path.join(r, file)
                relative_path = os.path.relpath(p,root)
                line = "\t" + "${TENSORFLOW_LITE_MICRO_DIR}/" + relative_path + "\n"
                out.write(line)
    out.write('''
  )

endif()''')