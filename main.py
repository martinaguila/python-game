import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import random
import time
from kivy.uix.label import Label

Builder.load_string("""
<MainScreen>:	
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'Welcome to Niko Mini Games'		
			background_color: 1, 1, 1, 1
			font_size: 50
		Label: 
			text: ''
		Button:
			text: 'Play Color Picker'
			on_press: root.manager.current = 'gamescreen'
			background_color: .06, 0, .7, 1
			font_size: 40
		Button:
			text: 'Play Type The Word'
			on_press: root.manager.current = 'gamescreen2'
			background_color: 1, .9, 0, 1
			font_size: 40
		Button:
			text: 'Play Guess the Logo'
			on_press: root.manager.current = 'playlogo'
			background_color: 1, .6, 0, 1
			font_size: 40
		Label:
			text: ''
		Button:
			background_color: .7, 0, 0, 1
			text: 'Exit'
			font_size: 40
			on_press: root.exitApp()
		Label:
			text: ''
			

<GameScreen>:
    BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'Color Picker'
			background: .06, 0, .7, 1
			font_size: 50
		Label:
			text: 'Press PLAY! to Start'
			id: lblOutput
			font_size: 40
		Button:
			text: 'PLAY!'
			on_press: root.play()
			background_color: .6, .8, .9, 1
			font_size: 40
		BoxLayout:
			orientation: 'horizontal'
			Label:
				text: 'Time: '
				id: lblTime
				font_size: 40
			Label:
				text: '0'
				id: lblScore
				value: 0
				font_size: 40
			Label:
				text: 'Message!'
				id: lblMessage
				font_size: 40
		GridLayout:
			rows: 2
			Button: 
				text: 'RED'
				id: cRed
				on_press: root.cred()
				background_color: 1, 0, 0, 1
			Button: 
				text: 'GREEN'
				id: cGreen
				on_press: root.cgreen()
				background_color: 0, 1, 0, 1
			Button:
				text: 'BLUE'
				id: cBlue
				on_press: root.cblue()
				background_color: 0, 0, 1, 1
			Button:
				text: 'YELLOW'
				id: cYellow
				on_press: root.cyellow()
				background_color: 1, 1, 0, 1
			Button:
				text: 'ORANGE'
				id: cOrange
				on_press: root.corange()
				background_color: 1, .6, 0, 1
			Button:
				text: 'PURPLE'
				id: cPurple
				on_press: root.cpurple()
				background_color: .6, .1, 1, 1
		BoxLayout:
			orientation: 'vertical'
			Label:
				text: ''
		GridLayout:
			cols: 2
			Button:
				text: 'Reset'
				background_color: 0, .5, .5, 1
				font_size: 40
				on_press: root.mainReset()
			Button:
				text: 'Back'
				on_press: root.manager.current = 'mainscreen'
				background_color: .7, 0, 0, 1
				font_size: 40
				on_press: root.mainBack()
		Label:
			text: ''

<GameScreen2>:
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'Welcome to Type the Word'
			font_size: 50
		Label:
			text: 'Press PLAY! to Start'
			id: lblOutput2
			font_size: 40
		Button:
			text: 'PLAY!'
			on_press: root.play2()
			background_color: .6, .8, .9, 1
			font_size: 40
		BoxLayout:
			orientation: 'horizontal'
			Label:
				text: 'Time: '
				id: lblTime2
				font_size: 40
			Label:
				text: '0'
				id: lblScore2
				value: 0
				font_size: 40
			Label:
				text: 'Message!'
				id: lblMessage2
				font_size: 40
		GridLayout:
			cols: 2
			TextInput:
				id: txtWord
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: 'Enter Word'
					on_press: root.btnEnter()
					background_color: .6, .8, .1, 1
					font_size: 40
				Button:
					text: 'Clear Text'
					on_press: root.clear()
					background_color: 0, .5, .5, 1
					font_size: 40
		BoxLayout:
			orientation: 'vertical'
			Button:
				text: 'Back'
				on_press: root.manager.current = 'mainscreen'
				background_color: .7, 0, 0, 1
				font_size: 40
				on_press: root.backMain2()
		Label:
			text: ''

<playLogo>:
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'Welcome to Guess the Logo'
			font_size: 50
		GridLayout:
			cols: 6
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:				
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
		GridLayout:
			cols: 6
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:				
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
		GridLayout:
			cols: 6
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:				
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
			BoxLayout:
				orientation: 'vertical'
				Button:
					text: '1'
				TextInput:
		BoxLayout:
			Label:
				text: ''
		BoxLayout:
			Button:
				orientation: 'horizontal'
				text: 'Back'
				on_press: root.manager.current = 'mainscreen'
				background_color: .7, 0, 0, 1
				font_size: 40
		BoxLayout:
			Label:
				text: ''

""")




# Declare both screens
class MainScreen(Screen):
	pass


class GameScreen(Screen):
	
	def play(self):
		timer = int(2)

		myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
		bro = random.choice(myList)
		self.ids.lblOutput.text = str(bro)

		for i in range(timer):
			self.ids.lblTime.text = str(timer - i)
			self.ids.lblTime.text = str(timer)
			time.sleep(1)
			

		
	def cred(self):
		theOutput = self.ids.lblOutput.text
		value = self.ids.lblScore.text
		if theOutput == "RED":
			self.ids.lblScore.text = str(int(value) + 1)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
		if theOutput != "RED":
			self.ids.lblScore.text = str(int(value) -2)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)

	def cgreen(self):
		theOutput = self.ids.lblOutput.text
		value = self.ids.lblScore.text
		if theOutput == "GREEN":
			self.ids.lblScore.text = str(int(value) + 1)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
		if theOutput != "GREEN":
			self.ids.lblScore.text = str(int(value) -2)  
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)  
			myMessage = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)


	def corange(self):
		theOutput = self.ids.lblOutput.text
		value = self.ids.lblScore.text
		if theOutput == "ORANGE":
			self.ids.lblScore.text = str(int(value) + 1)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
		if theOutput != "ORANGE":
			self.ids.lblScore.text = str(int(value) -2)  
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
  

	def cyellow(self):
		theOutput = self.ids.lblOutput.text
		value = self.ids.lblScore.text
		if theOutput == "YELLOW":
			self.ids.lblScore.text = str(int(value) + 1)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
		if theOutput != "YELLOW":
			self.ids.lblScore.text = str(int(value) -2)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro) 
			myMessage = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
   

	def cblue(self):
		theOutput = self.ids.lblOutput.text
		value = self.ids.lblScore.text
		if theOutput == "BLUE":
			self.ids.lblScore.text = str(int(value) + 1)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
		if theOutput != "BLUE":
			self.ids.lblScore.text = str(int(value) -2)  
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro) 
			myMessage = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
 

	def cpurple(self):
		theOutput = self.ids.lblOutput.text
		value = self.ids.lblScore.text
		if theOutput == "PURPLE":
			self.ids.lblScore.text = str(int(value) + 1)
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)
		if theOutput != "PURPLE":
			self.ids.lblScore.text = str(int(value) -2)  
			myList = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'ORANGE', 'PURPLE']
			bro = random.choice(myList)
			self.ids.lblOutput.text = str(bro)
			myMessage = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg = random.choice(myMessage)
			self.ids.lblMessage.text = str(msg)

	def mainBack(self):
		self.ids.lblScore.text = str('0')
		self.ids.lblMessage.text = str('Message!')
		self.ids.lblOutput.text = str('Press PLAY! to Start')

	def mainReset(self):
		self.ids.lblScore.text = str('0')
		self.ids.lblMessage.text = str('Message!')
		self.ids.lblOutput.text = str('Press PLAY! to Start')

	
class GameScreen2(Screen):
	
	def play2(self):
		myList = ['batkaandito', 'anongginagawamo', 'subukanmolang', 'samalayoangtingin', 'huwagmonangnaisin', 'pustahanpatayo', 'pinatuyongitlogngkabayo', 'magintaynaman', 'gawinnaangdapatgawin']
		bro2 = random.choice(myList)
		self.ids.lblOutput2.text = str(bro2)

	def btnEnter(self):
		myList = ['batkaandito', 'anongginagawamo', 'subukanmolang', 'samalayoangtingin', 'huwagmonangnaisin', 'pustahanpatayo', 'pinatuyongitlogngkabayo', 'magintaynaman', 'gawinnaangdapatgawin']
		bro2 = random.choice(myList)	
		word = self.ids.txtWord.text
		output = self.ids.lblOutput2.text
		value2 = self.ids.lblScore2.text
		if str(output) == str(word):
			myList = ['batkaandito', 'anongginagawamo', 'subukanmolang', 'samalayoangtingin', 'huwagmonangnaisin', 'pustahanpatayo', 'pinatuyongitlogngkabayo', 'magintaynaman', 'gawinnaangdapatgawin']
			bro2 = random.choice(myList)
			self.ids.lblOutput2.text = str(bro2)
			self.ids.lblScore2.text = str(int(value2) + 1)
			myMessage2 = ['AWESOME!', 'NICE!', 'GOOD JOB!', 'VERY GOOD!', 'OUTSTANDING!']
			msg2 = random.choice(myMessage2)
			self.ids.lblMessage2.text = str(msg2)
	
		if str(output) != str(word):
			self.ids.lblScore2.text = str(int(value2) - 2)
			myMessage2 = ['NOPE!', 'WRONG!', 'POOR!', 'VERY BAD!', 'NOT GOOD!']
			msg2 = random.choice(myMessage2)
			self.ids.lblMessage2.text = str(msg2)


	def clear(self):
		self.ids.txtWord.text = str('')

	def backMain2(self):
		self.ids.lblScore2.text = str('0')
		self.ids.lblMessage2.text = str('Message!')
		self.ids.lblOutput2.text = str('Press PLAY! to Start')
		self.ids.txtWord.text = str('')

class playLogo(Screen):
	pass
		

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name="mainscreen"))
sm.add_widget(GameScreen(name="gamescreen"))
sm.add_widget(GameScreen2(name="gamescreen2"))
sm.add_widget(playLogo(name="playlogo"))



class TestApp(App):

    def build(self):
	    
        return sm

if __name__ == '__main__':
    TestApp().run()