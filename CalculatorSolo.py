# Пробую написати калькулятор без відео - урока

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.config import Config
Config.set("graphics","resizable",0)
Config.set("graphics","width","300")
Config.set("graphics","height","400")

class CalculatorApp(App):
	def CalcReset(self,instance):
		self.formula = "0"
		self.UpdateLabel()

	def CalcResult(self,instance):
		self.lbl.text = str(eval(self.lbl.text))
		self.formula = "0"

	def AddOperation(self,instance):
		if (str(instance.text).lower() == "x"):
			self.formula += "*"
			self.UpdateLabel()
		elif(str(instance.text).lower() == "x²"):
			self.formula += "**"
			self.UpdateLabel()
		else:
			self.formula += str(instance.text)

			self.UpdateLabel()

	def UpdateLabel(self):
		self.lbl.text = self.formula

	def AddNumber(self,instance):
		if (self.formula == "0"):
			self.formula = ""

		self.formula += str(instance.text)

		self.UpdateLabel()

	def build(self):
		self.formula = "0"

		bl = BoxLayout(orientation = "vertical",
							padding = 10,)
		gl = GridLayout(cols = 4,
							padding = 10,
							spacing = 3,
							size_hint = (1,.7))
		self.lbl = (Label(text = "0",
							halign = "right",
							valign = "center",
							size_hint = (1,.3),
							text_size = (300 - 20,400 * .3 - 20),
							font_size = 35))

		bl.add_widget(self.lbl)

		
		bl.add_widget(gl)

		gl.add_widget(Button(text = "//",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))
		gl.add_widget(Button(text = "X²",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))
		gl.add_widget(Button(text = "%",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))
		gl.add_widget(Button(text = "C",
								on_press = self.CalcReset,
								background_color = [.22, 0, .30, 1],
								background_normal = ""))
		


		gl.add_widget(Button(text = "7",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "8",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "9",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "X",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))

		gl.add_widget(Button(text = "4",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "5",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "6",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "/",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))

		gl.add_widget(Button(text = "1",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "2",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "3",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "+",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))

		gl.add_widget(Button(text = ".",
								on_press = self.AddNumber,
								background_color = [.90, .24, 0, 1],
								background_normal = ""))
		gl.add_widget(Button(text = "0",
								on_press = self.AddNumber,
								background_color = [1,0,0,1],
								background_normal = ""))
		gl.add_widget(Button(text = "=",
								on_press = self.CalcResult,
								background_color = [.90, .24, 0, 1],
								background_normal = ""))
		gl.add_widget(Button(text = "-",
								on_press = self.AddOperation,
								background_color = [0,0,1,1],
								background_normal = ""))

		return bl




CalculatorApp().run()