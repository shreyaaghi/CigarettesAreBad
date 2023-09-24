from PIL import Image
import PySimpleGUI as gui
import io
import os
from util import get_config

# load_image("images/refusal.png", window, "img")

config = get_config()
width, height = config['width'], config['height']

def information():
    font = {"Helvetica", 40}
    layout = [
        [gui.Button("Back", key="Information Back Button"), gui.Text("Information", font=font)],
        [gui.Multiline("The National Cancer Institute reports that over 90% of adult smokers started before age 18, emphasizing the alarming issue of teenage smoking. Experimenting with cigarettes can lead to severe health consequences. To prevent addiction, it's crucial to educate young people early about the risks and factors contributing to teen tobacco use. This section explores these aspects, aiming to empower both teenagers and their caregivers to make informed choices.", key="introText", write_only = True, font=font, disabled=True, size = (width//20, 12)), gui.Image(key="img")],
        [gui.Text("What is a Cigarette?", font=font)],
        [gui.Multiline("Tobacco is a plant which is grown for it's leaves, and when they are harvested they can be put in cigarettes. While there are other tobacco products, cigarettes are the most commonly used. When the cigarette is lighted at the end with tobacco, the smoke is inhaled on the other end (diagram to the left).", write_only = True, font=font, disabled=True, size = (width//20, 5)), gui.Image(key="carousel1")],
        [gui.Button("Previous Image", key="Previous Image Button"), gui.Button("Next Image", key="Next Image Button")],
        [gui.Text("What is a Vape?", font=font)],
        [gui.Multiline("A vape is an electronic form of a cigarette that can be refilled and reused. It contains an e-liquid that is heated up inside the vape and converted to an aerosol, which can then be inhaled by the user (see diagram below). Even though vaping is more recent than cigarette smoking, it has become increasing popular among youth in the past decade.", write_only = True, font=font, disabled=True, size = (width//20, 10))],
        [gui.Text("So, what's the difference?", font=font)],
        [gui.Multiline("Vapes can be used multiple times, and many newer versions can be recharged; additionally, the liquid that is inhaled into the lungs can be refilled. The biggest difference between vapes and cigarettes is that vapes do not contain tobacco.", write_only = True, font=font, disabled=True, size = (width//20, 10))],
        [gui.Multiline("While this may provide benefits for the environment, this does NOT mean that vaping is a perfectly healthy alternative to smoking. The e-liquid still contains all the chemicals and compounds that make smoking so dangerous, and it's use among teenagers has rapidly grown because of how easy it is to use. According to lung.org, nearly 2500 children under the age of 18 try their first cigarette daily, and more than 400 of them will become regular daily smokers.", write_only = True, font=font, disabled=True, size = (width//20, 10)), gui.Image(key="img3")],
        [gui.Text("What's Inside a Cigarette?", font=font)],
        [gui.Multiline("A diagram of some of the most prevalent substances found in cigarettes is shown below. Nicotine is the most significant of all of them because it's the cause behind tobacco addiction. It releases dopamine, which is a neurotransmitter that can cause a temporary uplift in mood. These chemicals are just few of all 7,000 chemicals produced by cigarettes. Some of the other impactful substances not listed in the diagram are formaldehyde, which can increase the risk of heart disease, and tar, which damages your lungs and causes various breathing issues.", write_only = True, font=font, disabled=True, size = (width//20, 10)), gui.Image(key="img2")] 

    ]
    return layout