# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 02:01:19 2017

@author: david
"""
'''
import wx
app = wx.App()
frame = wx.Frame(None,-1,'window name',style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION)
frame.Show()
app.MainLoop()
'''
import wx
class WindowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WindowClass, self).__init__(*args, **kwargs)
        
        self.basic_gui()

        

    
    def basic_gui(self):
        dic = {'c104018':{'aulas':{'domingo':'8:30','segunda':'10:30','quarta':'12:30'},'nome':['חשבון דיפרנציאלי ואינטגרלי 1מ','דר יוסי כהן']},'c104019':{'aulas':{'domingo':'10:30','terça':'10:30','quarta':'12:30'},'nome':['אלגברה לינארית מ','דר סילביה בהר']}}
        print(((dic['c104018'])['nome'])[0])
        panel = wx.Panel(self)  
        
        week = wx.Bitmap('semana_choice2.png')
        tela = wx.BitmapButton(panel,id=3,bitmap=week, size=(week.GetWidth(),week.GetHeight()),pos = (10,50))
        
        #plotweek = wx.Image(week, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.plotweek = wx.StaticBitmap(self, -1, plotweek, (30, 30))
        
        self.CreateStatusBar()
        self.SetStatusText('hello')
        
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        editMenu = wx.Menu()        
        
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Quit','Quit Application')
        
        
        menuBar.Append(fileMenu, '&File') #short key
        menuBar.Append(editMenu, 'Edit')
        
                
                    
            
        
        '''
        yesNo = wx.MessageDialog(None,'voce gosta de wxPython ?', 'pergunta', wx.YES_NO)
                
        
        yesNoAnswer = yesNo.ShowModal()
        yesNo.Destroy()
        
        if yesNoAnswer == wx.ID_NO:
            username = 'Looser!'
        '''
        '''
        chooseOnebox = wx.SingleChoiceDialog(None, 'qual sua cor favorita','questao de cor', ['red','blue','yellow','pink'])
        
        
        favColor = None        
        if chooseOnebox.ShowModal() == wx.ID_OK:
            favColor = chooseOnebox.GetStringSelection()
            print(favColor)
        
        chooseOnebox.Destroy()
        '''     
            
        #textArea = wx.TextCtrl(panel, pos=(10,10), size=(200,50))
        '''
        if favColor:
           textArea.AppendText('sua cor favorita eh '+ favColor)
        '''
        text = wx.StaticText(panel,-1,'Enter your courses',(850,70))        
        text.SetForegroundColour('blue')
        #text.SetBackgroundColour('black')
        
        
        #wx.Button(panel,1,'close', (190,90))        
        bmp = wx.Bitmap('fechar.png')
        button = wx.BitmapButton(panel,id=1,bitmap=bmp, size=(bmp.GetWidth(),bmp.GetHeight()),pos = (880,570))
        
        
        
        course = wx.Button(panel,2,'Add course', (850,90))
        preference = wx.Button(panel,5,'Choose preference', (950,90))  
        Find = wx.Button(panel,6,'Find', (900,300)) 
        
        preferencia = None   
        
        def test(list,panel):
            
            course = None
            nameDialog = wx.TextEntryDialog(None, 'Add courses', 'Hello','Course')
            l=130
            while nameDialog.ShowModal() == wx.ID_OK:
            
                course = nameDialog.GetValue()
                list.append(course)
                nameDialog = wx.TextEntryDialog(None, 'Add courses', 'Hello','Course')
                
                
                if str('c'+course) in dic:
                    
                    aweText = wx.StaticText(panel,-1,((dic['c'+str(course)])['nome'])[0] +'<-', (780,l))
                    
                else:
                    aweText = wx.StaticText(panel,-1,course, (900,l))
                aweText.SetForegroundColour('blue')
                aweText.SetBackgroundColour('white')
                l+=20
            #print(list)
            courses.append(list)
            #global courses
            return list
        
             
                 
            #print(lista)  
            nameDialog.Destroy()
        
            
        def choosePreference(x,panel):
            
            chooseOnebox = wx.SingleChoiceDialog(None, 'Your Preference','Preference', ['Finish at 12:30','Finish at 14:30','Lunch Break','Start at 10:30'])
            x = None
        
                
            if chooseOnebox.ShowModal() == wx.ID_OK:
                x = chooseOnebox.GetStringSelection()
                print(x)
                aweText = wx.StaticText(panel,-1,x, (960,130))
                aweText.SetForegroundColour('blue')
                aweText.SetBackgroundColour('white')
                
                
                return x
        
            chooseOnebox.Destroy()
        
        def rodar():
            pass
            
            
        
        courses = []
        self.Bind(wx.EVT_BUTTON, lambda avt:test(courses,panel) ,course)
        self.Bind(wx.EVT_BUTTON, lambda avt:choosePreference(preferencia,panel) ,preference)
        self.Bind(wx.EVT_BUTTON, lambda avt:rodar() ,Find)
        #test(courses,panel)
        print(courses)
        #print(preferencia)
                
                   
        
        
        #aweText = wx.StaticText(panel,-1,'super customizado', (10,90))
        #aweText.SetForegroundColour('black')
        #aweText.SetBackgroundColour('white')        
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.onQuit, exitItem)
        self.SetSize((1100, 700))        
        self.SetTitle('seja bem vindo ')  
        
        
        
        self.Bind(wx.EVT_BUTTON, self.onQuit,id=1)
        
                
        
        self.Centre()
        self.Show(True)
        #print(courses)
    def nome(self,e):
        courses = []
        course = None
        nameDialog = wx.TextEntryDialog(None, 'qual seu nome ?', 'seja bem vindo','Course')

        while nameDialog.ShowModal() == wx.ID_OK:
            
            course = nameDialog.GetValue()
            courses.append(course)
            nameDialog = wx.TextEntryDialog(None, 'qual seu nome ?', 'seja bem vindo','Course')
            print(course)
        return courses    
        nameDialog.Destroy()
        if nameDialog.ShowModal() == wx.ID_CANCEL:
            return courses
            nameDialog.Destroy()
        return courses
        
        
    
    def onQuit(self, e):
        self.Close()

    def lista_cursos(self,e):
        nameDialog = wx.TextEntryDialog(None, 'Enter your courses','bem vindo','Course')
        if nameDialog.ShowModal() == wx.ID_OK:
            course = nameDialog.GetValue()
        
        nome.Destroy()
    
    def postCursos(self):
        curso = wx.StaticText(panel,-1,curso, (870,90))
        curso.SetForegroundColour('black')
    
        
        
    
        
    
def main():
    app = wx.App()
    WindowClass(None)
    app.MainLoop()

main()
        
