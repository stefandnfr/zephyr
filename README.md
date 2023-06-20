# Custom Zepyhyr based software distribution

This is a fork from the original [zephyr-project](https://docs.zephyrproject.org/latest/develop/application/index.html#advanced-example-application-usage) for having an up to date tflite micro version available. 

## How to maintain
```
git merge upstream/main
```
manually update a fork of the tflite-micro [repository](https://github.com/tensorflow/tflite-micro) and include a directory named `zephyr` in root which includes a `module.yml` file containing the following:
```
name: tflite-micro
build:
  cmake-ext: True
  kconfig-ext: True

```
Then set remote for the tflite-micro module in this repository's `west.yml` file, like this:
```
remotes:
  - name: <your_upstream_name>
    url-base: https://github.com/<github_maintainer>

```
Next, change git repo information below in the same file:
```
    - name: tflite-micro
      remote: <your_upstream_name>
      revision: <git_commit_hash>
      path: modules/lib/tflite-micro
```

Alternatively, a somewhat maintained zephyr-compatible version can be found [here](https://github.com/stefandnfr/tflite-micro) and is already set in the `west.yml` file. 

Finally, make sure to modify the CMakeLists.txt file in `./modules/tflite-micro/` to contain the correct paths that work with the tflite micro version. The script path.py is supposed to help you generating a CMakeLists.txt that corresponds to the required version. 

## How to use
The maintained zephyr project can be used like this:
```
cd <home>
mkdir my-workspace
cd my-workspace
git clone https://github.com/<user>/<this_repo> zephyr
west init -l zephyr
```