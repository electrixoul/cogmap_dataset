# Adaptive Agent Testbed

![](./docs/5.png)

----

## 环境配置

1. 创建新的 conda 环境，并启动

   ```bash
   conda create -n cogmap
   conda activate cogmap
   ```

2. 配置 JAX

   1. 安装 JAX

      ```bash
      pip install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
      conda install cuda -c nvidia
      conda activate cogmap # re-activate conda env
      pip install flax
      pip install optax
      ```

   2. 设置环境变量

      第1种方式：通过 conda 设置虚拟环境变量

      ```bash
      conda env config vars set XLA_FLAGS=--xla_gpu_force_compilation_parallelism=1
      conda activate cogmap # re-activate conda env
      ```

      第2种方式：直接在命令行环境中设置（需要每次运行之前都做一次），仅限于第一种方法无效的情况下

      ```bash
      export XLA_FLAGS=--xla_gpu_force_compilation_parallelism=1
      ```

3. 其他必要依赖库的安装

   ```bash
   pip install numpy
   pip install opencv-python
   pip install -U tensorflow-gpu
   pip install scikit-learn
   pip install matplotlib
   pip install argparse
   ```

   **若遇到运行时的版本问题，请参考本文件末尾的完整 conda 环境包列表。**

4. 重启 conda 环境

   ```bash
   conda deactivate
   conda activate cogmap
   ```

## 目录说明

* 



## 运行在线学习任务



### 程序1：运行演示



### 程序2：特征分析































