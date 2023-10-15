from PIL import Image
import PySimpleGUI as gui
import io
import os
from util import get_config

# load_image("images/refusal.png", window, "img")

config = get_config()
width, height = config['width'], config['height']

def information():
    layout = [
        [gui.Button("Back", key="Information Back Button"), gui.Text("Information", font=("Helvetica",45))],
        [gui.Multiline("The National Cancer Institute reports that over 90% of adult smokers started before age 18, emphasizing the alarming issue of teenage smoking. Experimenting with cigarettes can lead to severe health consequences. To prevent addiction, it's crucial to educate young people early about the risks and factors contributing to teen tobacco use. This section explores these aspects, aiming to empower both teenagers and their caregivers to make informed choices.", key="introText", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//22, 10)), gui.Image(key="img")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text("What is a Cigarette?", font=("Helvetica",30))],
        [gui.Multiline("Tobacco is a plant which is grown for it's leaves, and when they are harvested they can be put in cigarettes. While there are other tobacco products, cigarettes are the most commonly used. When the cigarette is lighted at the end with tobacco, the smoke is inhaled on the other end (diagram to the right).", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//22, 6)), gui.Image(key="carousel1")],
        [gui.Text(size=(width//8, 12)), gui.Button("Previous Image", key="Previous Image Button"), gui.Button("Next Image", key="Next Image Button")],
        [gui.Text("What is a Vape?", font=("Helvetica",30))],
        [gui.Multiline("A vape is an electronic form of a cigarette that can be refilled and reused. It contains an e-liquid that is heated up inside the vape and converted to an aerosol, which can then be inhaled by the user (click 'next image' below the diagram at the top right). Even though vaping is more recent than cigarette smoking, it has become increasing popular among youth in the past decade.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 8))],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text("So, what's the difference?", font=("Helvetica",30))],
        [gui.Multiline("Vapes can be used multiple times, and many newer versions can be recharged; additionally, the liquid that is inhaled into the lungs can be refilled. The biggest difference between vapes and cigarettes is that vapes do not contain tobacco.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 7))],
        [gui.Multiline("While this may provide benefits for the environment, this does NOT mean that vaping is a perfectly healthy alternative to smoking. The e-liquid still contains all the chemicals and compounds that make smoking so dangerous, and it's use among teenagers has rapidly grown because of how easy it is to use. According to lung.org, nearly 2500 children under the age of 18 try their first cigarette daily, and more than 400 of them will become regular daily smokers.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 10)), gui.Image(key="img3")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text("What's Inside a Cigarette?", font=("Helvetica",30))],
        [gui.Text(" ")],
        [gui.Multiline("A diagram of some of the most prevalent substances found in cigarettes is shown below. Nicotine is the most significant of all of them because it's the cause behind tobacco addiction. It releases dopamine, which is a neurotransmitter that can cause a temporary uplift in mood. These chemicals are just few of all 7,000 chemicals produced by cigarettes. Some of the other impactful substances not listed in the diagram are formaldehyde, which can increase the risk of heart disease, and tar, which damages your lungs and causes various breathing issues.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 10)), gui.Graph(canvas_size = (500,300), graph_bottom_left = (0,0), graph_top_right = (500,300), change_submits = True, drag_submits=True, key="img2")],
        [gui.Text(" ")],
        [gui.Text("Advertising", font=("Helvetica", 30))],
        [gui.Text(" ")],
        [gui.Multiline("The tobacco industry has implemented many marketing strategies to get teens hooked on smoking and vaping. Here are 3 tactics that can lead from trying the first cigarette to a life-long addiction:\n\n\nVaping has become much more complex, and e-cigarettes can be made with different flavors and candies such as vanilla, cherry, chocolate, blueberry, and more. Colorful ads with pictures of fresh and sweet foods mislead readers and appeal to younger audiences.\n\nFamous celebrities can be seen on magazine covers and billboards holding a cigarette, which can have an influence on kids and teenagers who want to be just like their favorite celebrities.\n\nMany versions of cigarettes are advertised as a healthier alternative to regular smoking by using less tar and calling them “light cigarettes”. However, they are equally dangerous and can still kill you.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//13, 15))],
        [gui.Image(key="img4"), gui.Image(key="img5"), gui.Image(key="img6")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text("Diseases/Health Issues", font=("Helvetica", 30))],
        [gui.Multiline("Smoking is the number one cause of preventable deaths in the United States; over 480,000 lives are lost to cigarettes every year (source: CDC). Smoking and vaping affects all parts of the body and causes chronic illnesses/diseases (diagram on left). There are also short-term effects to smoking, such as bad breath, fatigue, coughing, shortness of breath, and even reduced taste and smell senses.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 9)), gui.Image(key = "img7")],
        [gui.Multiline("Smoking is also an issue for people exposed to it. Second-hand smoke can put people at higher risk of heart and breathing problems. According to the CDC, “there is no safe level of exposure to secondhand smoke”, meaning that the exposed can potentially suffer from many harmful health effects.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 8)), gui.Image(key = "img8")],
        [gui.Multiline("Over 70 percent of young adults have smoked a cigarette at least once. The road down tobacco addiction often begins at a young age, and there are many reasons behind this. \n\nThe prefrontal cortex is an area in your brain responsible for executive functions and decision making. It finishes developing at around 25 or 26, and that is why adults are more likely to make rational choices. Teenagers are more likely to become addicted due to their impulsive decision-making, and it can lead to psychiatric disorders and brain issues later on in life.\n\nAdditionally, smoking can be seen as a way to rebel against parents by showing independence. Friends can often peer pressure each other into smoking because it's considered 'cool' and everyone else is doing it. Engaging in these activities helps teenagers feel like they fit in with the social scene and it can be a temporary escape from stressors in life since dopamine is released. These influences can cause poor-decision making and severely impact teens in the long run.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 19)), gui.Image(key="img9")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text(" ")],
        [gui.Text("Conclusion", font=("Helvetica",30))],
        [gui.Multiline("Now that you understand the basics of nicotine addiction and smoking, the impact it has on teenagers and their well-being is clear. Smoking has developed since it originated in 3000 BC, and the products have become increasingly more modern and easy to use, while it still remains equally as dangerous. The teenage years are the most important part of an adolescents life, and the choices they make are crucial can determine the outcome of their health in the years to come. By helping them make the right decisions and keeping them informed on the dangers of tobacco, we can begin taking the steps to eliminate nicotine addiction and keep our teenagers future's safe.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//20, 12)), gui.Image(key="img10")]

    ]
    return layout