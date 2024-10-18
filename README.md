# 视频处理

... 正在开发中，未完成，催更请提 issue...

> 示例代码可以参看`main.ipynb`

## WEB 功能

- 提取视频中音频，并保存
- 给音频添加背景音乐，并保存
- 字幕识别/翻译，并保存

> 会尽快开发完成上传，暂且占个坑~

## 安装依赖

- 配置环境

  ```shell
  conda create -n movie_edit python=3.12
  conda activate movie_edit

  pip install -r requirements.txt
  ```

- 安装 `imagemagick`

  - [imagemagick 官网](https://www.imagemagick.org/script/download.php)
  - [安装教程 (win/linux/mac)](https://blog.csdn.net/DWBCZ/article/details/113914857)

## 字幕翻译

> 所有适配 API 接口的大模型厂商皆可

推荐使用 Siliconflow（[注册地址](https://cloud.siliconflow.cn/i/7v2WmxND)），可以白嫖 `Qwen/Qwen2.5-72B-Instruct` 等模型（[模型列表](https://siliconflow.cn/zh-cn/models)）

修改 `.env` 文件中的 `OPENAI_API_KEY`,`OPENAI_BASE_URL`

## 参考/致谢

- [streamlit](https://streamlit.io/)
- [siliconflow](https://siliconflow.cn/zh-cn/)
- [https://github.com/WEIFENG2333/AsrTools](https://github.com/WEIFENG2333/AsrTools)
