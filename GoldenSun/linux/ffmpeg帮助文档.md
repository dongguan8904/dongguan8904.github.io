超级快速音频和视频编码器

用法:
```sh
 ffmpeg [选项] [[输入文件选项] -i 输入文件]... {[输出文件选项] 输出文件}...
```

获取帮助:
- `-h`      -- 打印基本选项
- `-h long` -- 打印更多选项
- `-h full` -- 打印所有选项（包括所有格式和编解码器的特定选项，非常长）
- `-h type=name` -- 打印指定解码器/编码器/解复用器/复用器/滤波器/比特流过滤器/协议的所有选项
- 查看 `man ffmpeg` 以获取选项的详细描述。

打印帮助 / 信息 / 功能:
- `-L`                  显示许可证
- `-h topic`            显示帮助
- `-? topic`            显示帮助
- `-help topic`         显示帮助
- `--help topic`        显示帮助
- `-version`            显示版本
- `-buildconf`          显示构建配置
- `-formats`            显示可用格式
- `-muxers`             显示可用复用器
- `-demuxers`           显示可用解复用器
- `-devices`            显示可用设备
- `-codecs`             显示可用编解码器
- `-decoders`           显示可用解码器
- `-encoders`           显示可用编码器
- `-bsfs`               显示可用比特流过滤器
- `-protocols`          显示可用协议
- `-filters`            显示可用滤波器
- `-pix_fmts`           显示可用像素格式
- `-layouts`            显示标准通道布局
- `-sample_fmts`        显示可用音频采样格式
- `-dispositions`       显示可用流布局
- `-colors`             显示可用颜色名称
- `-sources device`     列出输入设备的来源
- `-sinks device`       列出输出设备的汇聚点
- `-hwaccels`           显示可用的硬件加速方法

全局选项（影响整个程序而不仅仅是一个文件）:
- `-loglevel loglevel`  设置日志级别
- `-v loglevel`         设置日志级别
- `-report`             生成报告
- `-max_alloc bytes`    设置单个分配块的最大大小
- `-y`                  覆盖输出文件
- `-n`                  从不覆盖输出文件
- `-ignore_unknown`     忽略未知的流类型
- `-filter_threads`     非复杂滤波器线程的数量
- `-filter_complex_threads`  -filter_complex的线程数量
- `-stats`              在编码期间打印进度报告
- `-max_error_rate maximum error rate`  解码错误的比例（0.0: 无错误, 1.0: 100%错误），超过此比例时ffmpeg返回错误而不是成功。

每个文件的主要选项:
- `-f fmt`              强制格式
- `-c codec`            编解码器名称
- `-codec codec`        编解码器名称
- `-pre preset`         预设名称
- `-map_metadata outfile[,metadata]:infile[,metadata]`  从输入文件设置输出文件的元数据信息
- `-t duration`         录制或转码“duration”秒的音频/视频
- `-to time_stop`       录制或转码停止时间
- `-fs limit_size`      设置文件大小限制（以字节为单位）
- `-ss time_off`        设置开始时间偏移
- `-sseof time_off`     设置相对于文件结尾的开始时间偏移
- `-seek_timestamp`     启用/禁用使用 `-ss` 按时间戳搜索
- `-timestamp time`     设置录制时间戳（使用“now”设置当前时间）
- `-metadata string=string`  添加元数据
- `-program title=string:st=number...`  添加指定流的节目
- `-target type`        指定目标文件类型（"vcd", "svcd", "dvd", "dv" 或 "dv50"，可选前缀 "pal-", "ntsc-" 或 "film-"）
- `-apad`               音频填充
- `-frames number`      设置输出帧数
- `-filter filter_graph`  设置流过滤器图
- `-filter_script filename`  从文件读取流过滤器图描述
- `-reinit_filter`      输入参数变化时重新初始化过滤器图
- `-discard`            丢弃
- `-disposition`        处置

视频选项:
- `-vframes number`     设置输出的视频帧数
- `-r rate`             设置帧率（Hz 值，分数或缩写）
- `-fpsmax rate`        设置最大帧率（Hz 值，分数或缩写）
- `-s size`             设置帧大小（WxH 或缩写）
- `-aspect aspect`      设置纵横比（4:3，16:9 或 1.3333，1.7777）
- `-display_rotation angle`  设置流的逆时针旋转角度（度数）
- `-display_hflip`      设置流的水平翻转（如果未设置，则覆盖任何显示旋转）
- `-display_vflip`      设置流的垂直翻转（如果未设置，则覆盖任何显示旋转）
- `-vn`                 禁用视频
- `-vcodec codec`       强制视频编解码器（“copy”表示复制流）
- `-timecode hh:mm:ss[:;.]ff`  设置初始时间码值
- `-pass n`             选择传递次数（1 到 3）
- `-vf filter_graph`    设置视频滤波器
- `-b bitrate`          视频比特率（请使用 `-b:v`）
- `-dn`                 禁用数据

音频选项:
- `-aframes number`     设置输出的音频帧数
- `-aq quality`         设置音频质量（特定于编解码器）
- `-ar rate`            设置音频采样率（以 Hz 为单位）
- `-ac channels`        设置音频通道数
- `-an`                 禁用音频
- `-acodec codec`       强制音频编解码器（“copy”表示复制流）
- `-ab bitrate`         音频比特率（请使用 `-b:a`）
- `-af filter_graph`    设置音频滤波器

字幕选项:
- `-s size`             设置帧大小（WxH 或缩写）
- `-sn`                 禁用字幕
- `-scodec codec`       强制字幕编解码器（“copy”表示复制流）
- `-stag fourcc/tag`    强制字幕标签/fourcc
- `-fix_sub_duration`   修正字幕持续时间
- `-canvas_size size`   设置画布大小（WxH 或缩写）
- `-spre preset`        将字幕选项设置为指定的预设

