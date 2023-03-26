import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3

# define the conversation rules
def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()


#say(""" first of all let me tell you Monet style images are images that are reminiscent of the artistic style of the famous French painter Claude Monet. Monet was a key figure in the development of the Impressionist movement in art, and his style is characterized by loose brushwork, bold colors, and a focus on capturing the impression of a scene rather than a literal representation.

#In terms of photography or digital art, Monet style images may use techniques such as blurring, softening, and color manipulation to create a dreamy, impressionistic effect. They may also incorporate natural elements such as flowers, water, and landscapes to evoke a sense of tranquility and harmony with nature. Overall, Monet style images aim to capture the essence of a moment or scene rather than providing a strictly realistic representation.""")
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello",
        ["Hi there! How can I assist you today?"]
    ],
    [
        r"what is your name?",
        ["My name is Bot, how can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking. How can I assist you?"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm based in California, how about you?"]
    ],
    [
        r"quit",
        ["Goodbye, have a great day!"]
    ],
[
        r"what is monestyle image",
        ["""first of all let me tell you Monet style images are images that are reminiscent of the artistic style of the famous French painter Claude Monet. Monet was a key figure in the development of the Impressionist movement in art, and his style is characterized by loose brushwork, bold colors, and a focus on capturing the impression of a scene rather than a literal representation.

In terms of photography or digital art, Monet style images may use techniques such as blurring, softening, Monet style images aim to capture the essence of a moment or scene rather than providing a strictly realistic representation."""]
    ],
[
        r"(.*) (name of your project|what you made) ?",
        ["monet syle image generator AI!"]
    ],

    [
        r"what is full form of gan",
        ["Generative adversarial networks"]
    ],
[
        r"what is gan| what do you mean by gan",
        ["""Generative adversarial networks Generative adversarial networks (GANs) are an exciting recent innovation in machine learning. GANs are generative models: they create new data instances that resemble your training data. For example, GANs can create images that look like photographs of human faces, even though the faces don't belong to any real person."""]
    ],
[
        r"how gan works",
        ["Generative adversarial networks GANs achieve this level of realism by pairing a generator, which learns to produce the target output, with a discriminator, which learns to distinguish true data from the output of the generator. The generator tries to fool the discriminator, and the discriminator tries to keep from being fooled."]
    ],
[
        r"what i should follow to learn gan",
        ["""Understand the difference between generative and discriminative models.
Identify problems that GANs can solve.
Understand the roles of the generator and discriminator in a GAN system.
Understand the advantages and disadvantages of common GAN loss functions.
Identify possible solutions to common problems with GAN training.
Use the TF GAN library to make a GAN.   """]

    ],
[
        r"how does this model deployment occurred",
        ["""Since we built our models in PyTorch, at the end of training we can save the model weights in a .pt file. These weights can then be loaded into the web server, essentially allowing us to load the model as it existed during training, except now we are going to use it for inference.

When deploying a ML application, the difficulty no longer lies in the research code to build the model but rather in creating an environment where users can upload data to be passed through the model. In our case, we needed to allow the users to make a POST request to upload an image, and then we can have code that decodes the image bytes in the web server, giving us the image the user uploaded.   """]
    ],
]

# create the chatbot
chatbot = Chat(pairs, reflections)

# define the GUI
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",tk.END)
    if msg != '':
        ChatLog.config(state=tk.NORMAL)
        ChatLog.insert(tk.END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = say(chatbot.respond(msg))
        ChatLog.insert(tk.END, "Bot: " + res + '\n\n')
        ChatLog.config(state=tk.DISABLED)
        ChatLog.yview(tk.END)

base = tk.Tk()
base.title("Chatbot")

ChatLog = tk.Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

EntryBox = tk.Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

SendButton = tk.Button(base, font=("Verdana",12,'bold'), text="Send", width="10", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command=send )

# place the GUI components
scrollbar.place(x=476,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=470)
EntryBox.place(x=128, y=401, height=90, width=348)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
