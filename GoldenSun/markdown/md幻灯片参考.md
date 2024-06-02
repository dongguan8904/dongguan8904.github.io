---
class: beamer
---

-----------------
# 酷炫的演示

## 阿贝德·纳迪尔

{{ post.date_today }}

<!-- 整体幻灯片设计 -->
<style>
.slide {
background:url() no-repeat center center fixed; background-size: cover;
}
.slide_type_title {
background: slategrey;
}
</style>

-----------------

## 幻灯片标题

1. Markor的所有Markdown功能**也支持**幻灯片展示~~删除线~~_斜体_ `代码`
2. 使用三个以上的连字符（---）分隔空行开始新的幻灯片
3. 最后一张幻灯片也以连字符结束
4. 可以使用CSS配置所有和单个幻灯片的背景
5. 以横向模式打印/导出PDF
6. 通过在幻灯片（在`---`之后的行）开始时添加标题`# 标题`创建仅标题幻灯片

-----------------
## 带居中图片的幻灯片
* 图片可以通过在alt文本中添加'imghcenter'来居中，并通过'imgbig'使图片放大到页面大小
* 示例：`![文本 imghcenter imgbig 文本](a.jpg)`

![图片](file:///android_asset/img/flowerfield.jpg)

-----------------
## 带有渐变背景的页面
* 以及一张图片
* 使用CSS .slide_p4 { } 配置背景颜色/图片（4 = 幻灯片页码）

![图片](file:///android_asset/img/flowerfield.jpg)

<style> .slide_p4 { background: linear-gradient(to bottom, #11998e, #38ef7d); } </style>

-----------------
## 带有图片背景的页面
* 包含文字和表格

| 左对齐 | 中间对齐 | 右对齐 |
| :------------- | :-----------: | --------------: |
| 测试        | 测试        | 测试        |
| 测试        | 测试        | 测试        |

<style> 
.slide_p5 { background: url('file:///android_asset/img/schindelpattern.jpg') no-repeat center center fixed; background-size: cover; }
.slide_p5 > .slide_body > * { color: black; }
</style>

-----------------
