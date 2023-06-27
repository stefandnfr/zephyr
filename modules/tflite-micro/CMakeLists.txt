
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
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/array.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/core/api/op_resolver.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/core/api/tensor_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/core/api/error_reporter.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/core/api/flatbuffer_conversions.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/core/c/common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/schema/schema_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/kernel_util.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/tensor_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/portable_tensor_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/quantization_util.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/tensor_ctypes.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/reference/comparisons.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/kernels/internal/reference/portable_tensor_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/memory_helpers.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_allocation_info.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/flatbuffer_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_interpreter.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_resource_variable.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_op_resolver.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_allocator.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/debug_log.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_log.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/mock_micro_graph.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_graph.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_profiler.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/recording_micro_allocator.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_time.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/system_setup.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/fake_micro_context.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_context.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/micro_string.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/bluepill/debug_log.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/cortex_m_generic/debug_log.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/cortex_m_generic/micro_time.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/tools/tflite_flatbuffer_align_wrapper.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arena_allocator/single_arena_buffer_allocator.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arena_allocator/persistent_arena_buffer_allocator.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arena_allocator/non_persistent_arena_buffer_allocator.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arena_allocator/recording_single_arena_buffer_allocator.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/slice.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/pack.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/elementwise.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/unidirectional_sequence_lstm.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/lstm_eval_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/fully_connected_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/read_variable.cc	
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/split_v.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cast.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/transpose.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/round.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/conv.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/fill.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/split.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/mul_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/depth_to_space.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/pooling.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/resize_bilinear.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/reshape_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/dequantize_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceil.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/select.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/hard_swish_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/comparisons.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/activations.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/l2_pool_2d.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/dequantize.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/floor.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/space_to_depth.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/logical_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/circular_buffer.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/neg.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/kernel_util.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/div.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/quantize.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/unpack.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/logistic.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/mirror_pad.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/reduce.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cumsum.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/detection_postprocess_flexbuffers_generated_data.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/svdf.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/depthwise_conv_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/micro_tensor_utils.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/while.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/svdf_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/space_to_batch_nd.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/circular_buffer_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/logical.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/prelu.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/gather.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/var_handle.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/prelu_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/tanh.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/add_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/conv_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/transpose_conv.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/concatenation.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/fully_connected.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/leaky_relu_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/kernel_runner.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/reduce_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/leaky_relu.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/reshape.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/sub_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/activations_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/embedding_lookup.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/sub.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/if.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/squeeze.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/elu.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/resize_nearest_neighbor.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/broadcast_to.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/hard_swish.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/lstm_eval.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/squared_difference.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/floor_mod.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/expand_dims.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/exp.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/quantize_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/mul.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/shape.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/batch_to_space_nd.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/log_softmax.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/pad.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/detection_postprocess.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/gather_nd.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/circular_buffer_flexbuffers_generated_data.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/l2norm.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/broadcast_args.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/floor_div.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/strided_slice.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/depthwise_conv.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/zeros_like.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/call_once.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/softmax_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/logistic_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/assign_variable.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/add.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/softmax.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/pooling_common.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/add_n.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arg_min_max.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/maximum_minimum.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/test_data_generation/generate_circular_buffer_flexbuffers_data.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/test_data_generation/generate_detection_postprocess_flexbuffers_data.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/unidirectional_sequence_lstm.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/pooling.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/svdf.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/fully_connected.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/mul.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/depthwise_conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/add.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/cmsis_nn/softmax.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/mli_interface.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/pooling.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/scratch_buffers.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/mli_slicers.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/mli_interface_mli_20.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/fully_connected.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/scratch_buf_mgr.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/depthwise_conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/arc_mli/add.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/unidirectional_sequence_lstm.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/fully_connected_int8.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/softmax_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/pooling.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/quantize.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/logistic.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/reduce.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/svdf.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/depthwise_conv_hifi.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/pad_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/depthwise_conv_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/reduce_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/fully_connected_common_xtensa.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/transpose_conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/fully_connected.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/conv_hifi.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/leaky_relu.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/reshape.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/sub.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/conv_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/pooling_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/lstm_eval.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/softmax_int8_int16.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/fully_connected_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/pad.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/conv_int8_reference.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/strided_slice.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/depthwise_conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/conv_int16_reference.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/add.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/add_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/softmax.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/reshape_vision.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/lstm_eval_hifi.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/pooling_int8.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/hifimini/svdf.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/xtensa/hifimini/fully_connected.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/testdata/conv_test_data.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/testdata/lstm_test_data.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/ceva_common.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/quantize.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/logistic.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/fully_connected.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/depthwise_conv.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/kernels/ceva/softmax.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/memory_planner/non_persistent_buffer_planner_shim.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/memory_planner/linear_memory_planner.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/memory_planner/greedy_memory_planner.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/cortex_m_corstone_300/micro_time.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/cortex_m_corstone_300/system_setup.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/strided_slice/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/add/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/transpose_conv/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/quantize/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/sub/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/conv/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/pad/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/integration_tests/seanet/leaky_relu/integration_tests.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/benchmarks/keyword_benchmark_8bit.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/benchmarks/keyword_benchmark.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/benchmarks/person_detection_benchmark.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/testing/test_conv_model.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/chre/debug_log.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/riscv32_mcu/debug_log.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arc_custom/micro_time.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arc_custom/system_setup.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/ceva/micro_time.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/ceva/system_setup.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/python/tflite_size/src/flatbuffer_size_wrapper_pybind.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/python/tflite_size/src/flatbuffer_size_wrapper.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/python/tflite_size/src/flatbuffer_size.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/tflite_bridge/micro_error_reporter.cc
	${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/tflite_bridge/flatbuffer_conversions_bridge.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/micro/arc_emsdp/debug_log.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/frontend.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/fft.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/window_util.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/fft_io.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/log_scale_io.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/filterbank_io.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/fft_util.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/log_scale.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/filterbank.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/filterbank_util.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/log_lut.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/window.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/window_io.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/noise_reduction.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/frontend_io.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_main.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/log_scale_util.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_io.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/frontend_main.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_generator.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/kiss_fft_int16.cc
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/frontend_util.c
	# ${TENSORFLOW_LITE_MICRO_DIR}/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.c

  )

endif()