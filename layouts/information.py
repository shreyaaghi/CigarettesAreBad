from PIL import Image
import PySimpleGUI as gui
import io

img = Image.open('images/refusal.png')
img.thumbnail((100,100))
image_byte = io.BytesIO()
img.save(image_byte, format='PNG')
image_byte = image_byte.getvalue()


def information():
    font = {"Helvetica", 25}
    layout = [
        [gui.Button("Back", key="Information Back Button"), gui.Text("Information", font={"Helvetica",25})],
        [gui.Text("According to the National Cancer Institute, over 90% of daily adult cigarette smokers began smoking before the age of 18. This striking statistic highlights a deeply concerning trend: smoking among teenagers. What might seem like a harmless experiment or a brief habit can have extreme consequences for both health and well-being. By the time young adults are introduced to smoking, it can be too late. The best way to prevent the road down to addiction is to learn about it at an earlier age. In this section, we'll dive into the world of tobacco use among teenagers by exploring the factors that contribute to this behavior and the risks that come with it. By gaining insight into the reasons behind these choices and the potential impact on young lives, the goal is to help both teenagers and those who care about them to make informed decisions.", font={"Helvetica",13})],
        [gui.Image(source = image_byte)]
    ]
    return layout