from tkinter import *
from tkinter import filedialog
from Curto_Circuito import calculo_curto
import csv

class CSV_creator(Frame):

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master

        self.master.title('Análise de Curto-Circuito')        
        self.master.geometry('1280x480')
           
        self.screen_Height = 460
        self.screen_Width = 1260

        self.canvas = Canvas(self.master, height=self.screen_Height, width=self.screen_Width)
        self.canvas.grid(row = 0, column = 0)

        self.scrollbarx = Scrollbar (self.master, orient = 'horizontal', command=self.canvas.xview)
        self.scrollbarx.grid(row = 1, column = 0, sticky = 'ew')
        self.scrollbary = Scrollbar (self.master, orient = 'vertical', command=self.canvas.yview)
        self.scrollbary.grid(row = 0, column = 1, sticky = 'ns')
        
        self.canvas.config(xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)

        self.frame = Frame(self.canvas, height=self.screen_Height, width=self.screen_Width)
        self.frame.grid(row = 1, column = 0, sticky = 'nsew')
        self.canvas.create_window((0,0), window = self.frame, anchor='nw') 

        self.framebox_Button = Frame(self.frame)
        self.framebox_Button.grid(row = 1, column = 0, sticky = 'nsew')

        self.framebox_manager_Button = Frame(self.frame)
        self.framebox_manager_Button.grid(row = 0, column = 0, sticky = 'nsew')

        self.framebox_Content = Frame(self.frame)
        self.framebox_Content.grid(row = 2, column = 0, sticky = 'nsew')

        self.framebox_Barra = Listbox(self.framebox_Content)
        self.framebox_Barra.grid(row = 1, column = 0, sticky = 'nw')
        self.framebox_Barra.bind('<Return>', lambda event: self.inserir_Barra())
         
        self.framebox_Transformador = Listbox(self.framebox_Content)
        self.framebox_Transformador.grid(row = 1, column = 2, sticky = 'nw')
        self.framebox_Transformador.bind('<Return>', lambda event: self.inserir_Trafo())  

        self.framebox_Gerador = Listbox(self.framebox_Content)
        self.framebox_Gerador.grid(row = 1, column = 1, sticky = 'nw')
        self.framebox_Gerador.bind('<Return>', lambda event: self.inserir_Gerador())

        self.framebox_Linha = Listbox(self.framebox_Content)
        self.framebox_Linha.grid(row = 1, column = 3, sticky = 'nw')
        self.framebox_Linha.bind('<Return>', lambda event: self.inserir_Linha())     

        self.label1 = Label(self.framebox_Barra, text = 'Barras')
        self.label1.grid(row = 0, column = 0, sticky = 'w')
        self.label2 = Label(self.framebox_Barra, text = 'Barra')
        self.label2.grid(row = 1, column = 0, padx = 5)
        self.label3 = Label(self.framebox_Barra, text = 'Tensão')
        self.label3.grid(row = 1, column = 1, padx = 5)
        self.label31 = Label(self.framebox_Barra, text = 'Curto Circuito')
        self.label31.grid(row = 1, column = 2)

        self.label4 = Label(self.framebox_Transformador, text = 'Transformadores').grid(row = 0, column = 0, sticky = 'ew')
        self.label28 = Label(self.framebox_Transformador, text = 'ID').grid(row = 1, column = 0)
        self.label5 = Label(self.framebox_Transformador, text = 'Impedância Percentual').grid(row = 1, column = 1, padx = 5)
        self.label6 = Label(self.framebox_Transformador, text = 'Impedâcia Aterramento Primário').grid(row = 1, column = 2, padx = 5)
        self.label7 = Label(self.framebox_Transformador, text = 'Impedância Aterramento Secundário').grid(row = 1, column = 3, padx = 5)
        self.label8 = Label(self.framebox_Transformador, text = 'Tensão Primário').grid(row = 1, column = 4, padx = 5)
        self.label9 = Label(self.framebox_Transformador, text = 'Tensão Secundário').grid(row = 1, column = 5, padx = 5)
        self.label10 = Label(self.framebox_Transformador, text = 'Potência do Transformador').grid(row = 1, column = 6, padx = 5)
        self.label11 = Label(self.framebox_Transformador, text = 'Tipo de Conexão').grid(row = 1, column = 7, padx = 5)
        self.label12 = Label(self.framebox_Transformador, text = 'Barra de Conexão Primário').grid(row = 1, column = 8, padx = 5)
        self.label13 = Label(self.framebox_Transformador, text = 'Barra de Conexão Secundário').grid(row = 1, column = 9, padx = 5)
        
        self.label14 = Label(self.framebox_Gerador, text ='Geradores').grid(row = 0, column = 0, sticky = 'w')
        self.label29 = Label(self.framebox_Gerador, text = 'ID').grid(row = 1, column = 0, sticky = 'w')
        self.label15 = Label(self.framebox_Gerador, text = 'Tensão').grid(row = 1, column = 1, sticky = 'w')
        self.label16 = Label(self.framebox_Gerador, text = 'Impedância Positiva').grid(row = 1, column = 2, sticky = 'w')
        self.label17 = Label(self.framebox_Gerador, text = 'Impedância Negativa').grid(row = 1, column = 3, sticky = 'w')
        self.label18 = Label(self.framebox_Gerador, text = 'Impedância Zero').grid(row = 1, column = 4, sticky = 'w')
        self.label19 = Label(self.framebox_Gerador, text = 'Impedância de Aterramento').grid(row = 1, column = 5, sticky = 'w')
        self.label20 = Label(self.framebox_Gerador, text = 'Conexão do Gerador').grid(row = 1, column = 6, sticky = 'w')
        self.label21 = Label(self.framebox_Gerador, text = 'Potência').grid(row = 1, column = 7, sticky = 'w')
        self.label22 = Label(self.framebox_Gerador, text = 'Barra de Conxexão').grid(row = 1, column = 8, sticky = 'w')

        self.label23 = Label(self.framebox_Linha, text = 'Linhas').grid(row = 0, column = 0, sticky = 'w')
        self.label24 = Label(self.framebox_Linha, text = 'ID').grid(row = 1, column = 0, sticky = 'w')
        self.label24 = Label(self.framebox_Linha, text = 'Impedância Positiva').grid(row = 1, column = 1, sticky = 'w')
        self.label25 = Label(self.framebox_Linha, text = 'Impedância Negativa').grid(row = 1, column = 2, sticky = 'w')
        self.label26 = Label(self.framebox_Linha, text = 'Impedancia Zero').grid(row = 1, column = 3, sticky = 'w')
        self.label25 = Label(self.framebox_Linha, text = 'Comprimento').grid(row = 1, column = 4, sticky = 'w')
        self.label26 = Label(self.framebox_Linha, text = 'Barra de Conexão Primário').grid(row = 1, column = 5, sticky = 'w')
        self.label27 = Label(self.framebox_Linha, text = 'Barra de Conexão Secundário').grid(row = 1, column = 6, sticky = 'w')

        self.bus = []
        self.voltage = []

        self.transformer = []
        self.impedance_T = []
        self.ground_primary_T = []
        self.ground_secondary_T = []
        self.voltage_primary_T = []
        self.voltage_secundary_T = []
        self.power_T = []
        self.type_con_T = []
        self.bus_primary_T = []
        self.bus_secondary_T = []

        self.generator = []
        self.voltage_G = []
        self.impedance_pos_G = []
        self.impedance_neg_G = []
        self.impedance_0_G = []
        self.ground_G = []
        self.type_con_G = []
        self.power_G = []
        self.bus_G = []

        self.wire = []
        self.impedance_pos_W = []
        self.impedance_neg_W = []
        self.impedance_0_W = []
        self.width_W = []
        self.bus_primary_W = []
        self.bus_secondary_W = []

        self.b1 = 1
        self.t1 = 1
        self.g1 = 1
        self.l1 = 1

        self.trifasico = BooleanVar()
        self.fase_Terra = BooleanVar()
        self.fase_Fase = BooleanVar()
        self.fase_fase_Terra = BooleanVar()

        self.entradas_Barras = []
        self.entradas_Transformador = []
        self.entradas_Gerador = []
        self.entradas_Linhas = []

        self.load = False
        self.save = False

        self.create_entries_Barras()
        self.create_entries_Trafo()
        self.create_entries_Gerador()
        self.create_entries_Linha()

        self.adicionar_Barra = Button(self.framebox_Content, text = 'Adicionar Barra', command=self.inserir_Barra)
        self.adicionar_Barra.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.adicionar_Barra.bind('<Return>', lambda event: self.inserir_Barra())

        self.adicionar_Trafo = Button(self.framebox_Content, text = 'Adicionar Transformador', command=self.inserir_Trafo)
        self.adicionar_Trafo.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.adicionar_Trafo.bind('<Return>', lambda event: self.inserir_Trafo())

        self.adicionar_Gerador = Button(self.framebox_Content, text = 'Adicionar Gerador', command=self.inserir_Gerador)
        self.adicionar_Gerador.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.adicionar_Gerador.bind('<Return>', lambda event: self.inserir_Gerador())

        self.adicionar_Linha = Button(self.framebox_Content, text = 'Adicionar Linha', command=self.inserir_Linha)
        self.adicionar_Linha.grid(row = 0, column = 3, padx = 10, pady = 10)
        self.adicionar_Linha.bind('<Return>', lambda event: self.inserir_Linha())

        self.carregar_arquivo = Button(self.framebox_manager_Button, text = 'Carregar último caso', command = self.load_csv)
        self.carregar_arquivo.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.carregar_arquivo = Button(self.framebox_manager_Button, text = 'Salvar caso', command = self.save_csv)
        self.carregar_arquivo.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.short_Circuit = Button(self.framebox_Button, text = 'Calcular Curto', command = self.solve_short)
        self.short_Circuit.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.sc_Triphase = Checkbutton(self.framebox_Button, text = 'Curto Trifásico', variable = self.trifasico, onvalue = True, offvalue = False, command = self.curto_Trifasico)
        self.sc_Triphase.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.sc_phase_Ground = Checkbutton(self.framebox_Button, text = 'Curto Fase-Terra', variable = self.fase_Terra, onvalue = True, offvalue = False, command = self.curto_fase_Terra)
        self.sc_phase_Ground.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.sc_phase_Phase = Checkbutton(self.framebox_Button, text = 'Curto Fase-Fase', variable = self.fase_Fase, onvalue = True, offvalue = False, command = self.curto_fase_Fase)
        self.sc_phase_Phase.grid(row = 0, column = 3, padx = 10, pady = 10)

        self.sc_phase_phase_Ground = Checkbutton(self.framebox_Button, text = 'Curto Fase-Fase-Terra', variable = self.fase_fase_Terra, onvalue = True, offvalue = False, command = self.curto_fase_fase_Terra)
        self.sc_phase_phase_Ground.grid(row = 0, column = 4, padx = 10, pady = 10)

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

        self.bind_all('<MouseWheel>', lambda event: self.canvas.yview_moveto(int(-1*(event.delta/120))), 'units')
        self.bind_all('<Shift-MouseWheel>', lambda event: self.canvas.xview_moveto(int(-1*(event.delta/120))),'units')
        self.bind('<Configure>', self.on_configure)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight = 1)       

    def on_configure(self):

        screen_height = self.winfo_screenheight() - 85
        screen_width = self.winfo_screenwidth() - 20

        self.canvas.config(height=screen_height, width=screen_width)
        self.frame.config(height=screen_height, width=screen_width)
        
        self.scrollbary.config(command=self.canvas.yview)
        self.scrollbarx.config(command=self.canvas.xview)

        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.canvas.update_idletasks()


    def solve_short(self):

        self.save_csv()

        calculo_curto.curto_circuito()

        self.curto_Trifasico()
        self.trifasico.set(True)
        
    def curto_Trifasico(self):

        cc_Trifasico = []

        with open('Curto_circuito.csv', newline='') as curto:
            
            reader_Curtot = csv.DictReader(curto)

            for rwct in reader_Curtot:
                cc_Trifasico.append(rwct['CC_Trifasico'])

        for st in range(len(cc_Trifasico)):
            self.short = Entry(self.framebox_Barra)
            self.short.insert(0, cc_Trifasico[st])
            self.short.grid(row = st + 2, column = 2, padx = 5, pady = 5)
            self.short.config(state = 'readonly')

        self.trifasico.set(True)
        self.fase_Terra.set(False)
        self.fase_Fase.set(False)
        self.fase_fase_Terra.set(False)

    def curto_fase_Terra(self):

        cc_fase_Terra = []

        with open('Curto_circuito.csv', newline='') as curtoterra:
            
            reader_Curtoft = csv.DictReader(curtoterra)

            for rwft in reader_Curtoft:
                cc_fase_Terra.append(rwft['CC_Fase_Terra'])

        for sf in range(len(cc_fase_Terra)):
            self.short = Entry(self.framebox_Barra)
            self.short.insert(0, cc_fase_Terra[sf])
            self.short.grid(row = sf + 2, column = 2, padx = 5, pady = 5)
            self.short.config(state = 'readonly')

        self.trifasico.set(False)
        self.fase_Terra.set(True)
        self.fase_Fase.set(False)
        self.fase_fase_Terra.set(False)

    def curto_fase_Fase(self):

        cc_fase_Fase = []

        with open('Curto_circuito.csv', newline='') as curtofase:
            
            reader_Curtoff = csv.DictReader(curtofase)

            for rwff in reader_Curtoff:
                cc_fase_Fase.append(rwff['CC_Fase_Fase'])

        for sff in range(len(cc_fase_Fase)):
            self.short = Entry(self.framebox_Barra)
            self.short.insert(0, cc_fase_Fase[sff])
            self.short.grid(row = sff + 2, column = 2, padx = 5, pady = 5)
            self.short.config(state = 'readonly')

        self.trifasico.set(False)
        self.fase_Terra.set(False)
        self.fase_Fase.set(True)
        self.fase_fase_Terra.set(False)

    def curto_fase_fase_Terra(self):

        cc_fase_fase_Terra = []

        with open('Curto_circuito.csv', newline='') as curtofft:
            
            reader_Curtofft = csv.DictReader(curtofft)

            for rwfft in reader_Curtofft:
                cc_fase_fase_Terra.append(rwfft['CC_Fase_Fase_Terra_A'])

        for sfft in range(len(cc_fase_fase_Terra)):
            self.short = Entry(self.framebox_Barra)
            self.short.insert(0, cc_fase_fase_Terra[sfft])
            self.short.grid(row = sfft + 2, column = 2, padx = 5, pady = 5)
            self.short.config(state = 'readonly')

        self.trifasico.set(False)
        self.fase_Terra.set(False)
        self.fase_Fase.set(False)
        self.fase_fase_Terra.set(True)

    def save_csv(self):

        if self.save == 'False':

            if self.barra.get() and self.tensao.get():
                self.bus.append(self.barra.get())
                self.voltage.append(self.tensao.get())

                with open('Barra.csv', mode = 'w', newline = '') as bar:
                    
                    writer_Bus = csv.DictWriter(bar, fieldnames = ['Barra', 'Tensao'])
                
                    writer_Bus.writeheader()

                    for z in range(len(self.bus)):
                        writer_Bus.writerow({'Barra': self.bus[z], 'Tensao': self.voltage[z]})

            if self.num_Trafo.get() and self.impedancia_Percentual.get():

                self.transformer.append(self.num_Trafo.get())
                self.impedance_T.append(self.impedancia_Percentual.get())
                
                if self.aterramento_Primario.get():
                    self.ground_primary_T.append(self.aterramento_Primario.get())
                else:
                    self.ground_primary_T.append(0)

                if self.aterramento_Secundario.get():
                    self.ground_secondary_T.append(self.aterramento_Secundario.get())
                else:
                    self.ground_secondary_T.append(0)
                
                self.voltage_primary_T.append(self.tensao_Primario.get())
                self.voltage_secundary_T.append(self.tensao_Secundario.get())
                self.power_T.append(self.potencia_Trafo.get())
                self.type_con_T.append(self.conexao_Trafo.get())
                self.bus_primary_T.append(self.barra_trafo_Primario.get())
                self.bus_secondary_T.append(self.barra_trafo_Secundario.get())

                with open('Transformador.csv', mode = 'w', newline = '') as tr:

                    writer_Transformer = csv.DictWriter(tr, fieldnames = ['Transformador','Impedancia_percentual','Impedancia_aterramento_primario','Impedancia_aterramento_secundario','Tensao primario','Tensao secundario','Potencia','Tipo_de_conexao','Conexao_primario','Conexao_secundario'])
                    writer_Transformer.writeheader()

                    for tx in range(len(self.transformer)):
                        writer_Transformer.writerow({'Transformador': self.transformer[tx],'Impedancia_percentual': self.impedance_T [tx],'Impedancia_aterramento_primario': self.ground_primary_T[tx],'Impedancia_aterramento_secundario': self.ground_secondary_T[tx],'Tensao primario': self.voltage_primary_T[tx],'Tensao secundario':self.voltage_secundary_T[tx],'Potencia': self.power_T[tx],'Tipo_de_conexao':self.type_con_T[tx],'Conexao_primario':self.bus_primary_T[tx],'Conexao_secundario':self.bus_secondary_T[tx]})

            if self.num_Gerador.get() and self.tensao_Gerador.get():

                self.generator.append(self.num_Gerador.get())
                self.voltage_G.append(self.tensao_Gerador.get())
                self.impedance_pos_G.append(self.impedancia_pos_Gerador.get())
                self.impedance_neg_G.append(self.impedancia_neg_Gerador.get())
                self.impedance_0_G.append(self.impedancia_z_Gerador.get())
                self.ground_G.append(self.ateramento_Gerador.get())
                self.type_con_G.append(self.conexao_Gerador.get())
                self.power_G.append(self.potencia_Gerador.get())
                self.bus_G.append(self.barra_Gerador.get())

                with open('Gerador.csv', mode = 'w', newline = '') as gen:

                    writer_Generator = csv.DictWriter(gen, fieldnames = ['Gerador','Tensao','Impedancia_positiva','Impedancia_negativa','Impedancia_zero','Impedancia_aterramento','Conexao_gerador','Potencia','Barra_conexao'])
                    writer_Generator.writeheader()

                    for gx in range(len(self.generator)):
                        writer_Generator.writerow({'Gerador': self.generator[gx],'Tensao': self.voltage_G[gx],'Impedancia_positiva': self.impedance_pos_G[gx],'Impedancia_negativa': self.impedance_neg_G[gx],'Impedancia_zero': self.impedance_0_G[gx],'Impedancia_aterramento': self.ground_G[gx],'Conexao_gerador': self.type_con_G[gx],'Potencia': self.power_G[gx],'Barra_conexao': self.bus_G[gx]})

            if self.num_Linha.get() and self.impedancia_Positiva.get():
                self.wire.append(self.num_Linha.get())
                self.impedance_pos_W.append(self.impedancia_Positiva.get())
                self.impedance_neg_W.append(self.impedancia_Negativa.get())
                self.impedance_0_W.append(self.impedancia_Zero.get())
                self.width_W.append(self.comprimento.get())
                self.bus_primary_W.append(self.barra_primario_Linha.get())
                self.bus_secondary_W.append(self.barra_secundario_Linha.get())

                with open('Linha.csv', mode = 'w', newline = '') as line:

                    writer_Wire = csv.DictWriter(line, fieldnames = ['Linha','Impedancia_positiva','Impedancia_negativa','Impedancia_zero','Comprimento','Primario','Secundario'])
                    writer_Wire.writeheader()

                    for lx in range(len(self.wire)):
                        writer_Wire.writerow({'Linha': self.wire[lx],'Impedancia_positiva': self.impedance_pos_W[lx],'Impedancia_negativa': self.impedance_neg_W[lx],'Impedancia_zero': self.impedance_0_W[lx],'Comprimento': self.width_W[lx],'Primario': self.bus_primary_W[lx],'Secundario': self.bus_secondary_W[lx]})
            
            self.save = True

    def inserir_Barra(self):

        if self.barra.get() and self.tensao.get():
            self.bus.append(self.barra.get())
            self.voltage.append(self.tensao.get())
        
        self.create_entries_Barras()

    def inserir_Trafo(self):

        if self.num_Trafo.get() and self.impedancia_Percentual.get():

            self.transformer.append(self.num_Trafo.get())
            self.impedance_T.append(self.impedancia_Percentual.get())
            
            if self.aterramento_Primario.get():
                self.ground_primary_T.append(self.aterramento_Primario.get())
            else:
                self.ground_primary_T.append(0)

            if self.aterramento_Secundario.get():
                self.ground_secondary_T.append(self.aterramento_Secundario.get())
            else:
                self.ground_secondary_T.append(0)
            
            self.voltage_primary_T.append(self.tensao_Primario.get())
            self.voltage_secundary_T.append(self.tensao_Secundario.get())
            self.power_T.append(self.potencia_Trafo.get())
            self.type_con_T.append(self.conexao_Trafo.get())
            self.bus_primary_T.append(self.barra_trafo_Primario.get())
            self.bus_secondary_T.append(self.barra_trafo_Secundario.get())

        self.create_entries_Trafo()

    def inserir_Gerador(self):

        if self.num_Gerador.get() and self.tensao_Gerador.get():

            self.generator.append(self.num_Gerador.get())
            self.voltage_G.append(self.tensao_Gerador.get())
            self.impedance_pos_G.append(self.impedancia_pos_Gerador.get())
            self.impedance_neg_G.append(self.impedancia_neg_Gerador.get())
            self.impedance_0_G.append(self.impedancia_z_Gerador.get())
            self.ground_G.append(self.ateramento_Gerador.get())
            self.type_con_G.append(self.conexao_Gerador.get())
            self.power_G.append(self.potencia_Gerador.get())
            self.bus_G.append(self.barra_Gerador.get())

        self.create_entries_Gerador()

    def inserir_Linha(self):

        if self.num_Linha.get() and self.impedancia_Positiva.get():
            self.wire.append(self.num_Linha.get())
            self.impedance_pos_W.append(self.impedancia_Positiva.get())
            self.impedance_neg_W.append(self.impedancia_Negativa.get())
            self.impedance_0_W.append(self.impedancia_Zero.get())
            self.width_W.append(self.comprimento.get())
            self.bus_primary_W.append(self.barra_primario_Linha.get())
            self.bus_secondary_W.append(self.barra_secundario_Linha.get())
        
        self.create_entries_Linha()

    def create_entries_Barras(self, size = None, barra_ID = None, tensao_Barra = None):

        self.save = False

        self.barra = Entry(self.framebox_Barra)
        self.tensao = Entry(self.framebox_Barra)
        self.short = Entry(self.framebox_Barra)
        self.entradas_Barras.append((self.barra))
        
        count = len(self.entradas_Barras) + 1

        if size is None:
            if self.load:    
                self.barra.grid(row = count, column = 0, padx = 5, pady = 5)
                self.barra.insert(END, self.b1 - 1)
                self.barra.config(state = 'readonly')
                self.tensao.grid(row = count, column = 1, padx = 5, pady = 5)
                self.short.grid(row = count, column = 2, padx = 5, pady = 5)

            else:
                self.barra.grid(row = count, column = 0, padx = 5, pady = 5)
                self.barra.insert(END, self.b1)
                self.barra.config(state = 'readonly')
                self.tensao.grid(row = count, column = 1, padx = 5, pady = 5)
                self.short.grid(row = count, column = 2, padx = 5, pady = 5)

        else:
            self.barra.insert(0,barra_ID)
            self.barra.grid(row = size + 2, column = 0, padx = 5, pady = 5)
            self.barra.config(state = 'readonly')
            self.tensao.insert(0,tensao_Barra)
            self.tensao.grid(row = size + 2, column = 1, padx = 5, pady = 5)
            self.short.grid(row = size + 2, column = 2, padx = 5, pady = 5)

        self.b1 += 1

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def create_entries_Trafo(self, trafo = None, impedancia = None, ground_Primario = None, ground_Secundario = None, V_Primario = None, V_Secundario = None, power_Trafo = None, con_Trafo = None, primario = None, secundario = None):
        
        self.save = False

        self.num_Trafo = Entry(self.framebox_Transformador)
        self.impedancia_Percentual = Entry(self.framebox_Transformador)
        self.aterramento_Primario = Entry(self.framebox_Transformador)
        self.aterramento_Secundario = Entry(self.framebox_Transformador)
        self.tensao_Primario = Entry(self.framebox_Transformador)
        self.tensao_Secundario = Entry(self.framebox_Transformador)
        self.potencia_Trafo = Entry(self.framebox_Transformador)
        self.conexao_Trafo = Entry(self.framebox_Transformador)
        self.barra_trafo_Primario = Entry(self.framebox_Transformador)
        self.barra_trafo_Secundario = Entry(self.framebox_Transformador)
        self.entradas_Transformador.append((self.impedancia_Percentual))

        count2 = len(self.entradas_Transformador) + 1

        if trafo is None:

            if self.load:
                self.num_Trafo.grid(row = count2, column = 0, padx = 5, pady = 5)
                self.num_Trafo.insert(END, self.t1-1)
                self.num_Trafo.config(state = 'readonly')
                self.impedancia_Percentual.grid(row = count2, column = 1, padx = 5, pady = 5)
                self.aterramento_Primario.grid(row = count2, column = 2, padx = 5, pady = 5)
                self.aterramento_Secundario.grid(row = count2, column = 3, padx = 5, pady = 5)
                self.tensao_Primario.grid(row = count2, column = 4, padx = 5, pady = 5)
                self.tensao_Secundario.grid(row = count2, column = 5, padx = 5, pady = 5)
                self.potencia_Trafo.grid(row = count2, column = 6, padx = 5, pady = 5)
                self.conexao_Trafo.grid(row = count2, column = 7, padx = 5, pady = 5)
                self.barra_trafo_Primario.grid(row = count2, column = 8, padx = 5, pady = 5)
                self.barra_trafo_Secundario.grid(row = count2, column = 9, padx = 5, pady = 5)

            else:
                self.num_Trafo.grid(row = count2, column = 0, padx = 5, pady = 5)
                self.num_Trafo.insert(END, self.t1)
                self.num_Trafo.config(state = 'readonly')
                self.impedancia_Percentual.grid(row = count2, column = 1, padx = 5, pady = 5)
                self.aterramento_Primario.grid(row = count2, column = 2, padx = 5, pady = 5)
                self.aterramento_Secundario.grid(row = count2, column = 3, padx = 5, pady = 5)
                self.tensao_Primario.grid(row = count2, column = 4, padx = 5, pady = 5)
                self.tensao_Secundario.grid(row = count2, column = 5, padx = 5, pady = 5)
                self.potencia_Trafo.grid(row = count2, column = 6, padx = 5, pady = 5)
                self.conexao_Trafo.grid(row = count2, column = 7, padx = 5, pady = 5)
                self.barra_trafo_Primario.grid(row = count2, column = 8, padx = 5, pady = 5)
                self.barra_trafo_Secundario.grid(row = count2, column = 9, padx = 5, pady = 5)
        
        else:
            self.num_Trafo.insert(END, trafo + 1)
            self.num_Trafo.grid(row = trafo + 2, column = 0, padx = 5, pady = 5)
            self.num_Trafo.config(state = 'readonly')
            self.impedancia_Percentual.insert(0,impedancia)
            self.impedancia_Percentual.grid(row = trafo + 2, column = 1, padx = 5, pady = 5)
            self.aterramento_Primario.insert(0,ground_Primario)
            self.aterramento_Primario.grid(row = trafo + 2, column = 2, padx = 5, pady = 5)
            self.aterramento_Secundario.insert(0,ground_Secundario)
            self.aterramento_Secundario.grid(row = trafo + 2, column = 3, padx = 5, pady = 5)
            self.tensao_Primario.insert(0,V_Primario)
            self.tensao_Primario.grid(row = trafo + 2, column = 4, padx = 5, pady = 5)
            self.tensao_Secundario.insert(0,V_Secundario)
            self.tensao_Secundario.grid(row = trafo + 2, column = 5, padx = 5, pady = 5)
            self.potencia_Trafo.insert(0,power_Trafo)
            self.potencia_Trafo.grid(row = trafo + 2, column = 6, padx = 5, pady = 5)
            self.conexao_Trafo.insert(0,con_Trafo)
            self.conexao_Trafo.grid(row = trafo + 2, column = 7, padx = 5, pady = 5)
            self.barra_trafo_Primario.insert(0,primario)
            self.barra_trafo_Primario.grid(row = trafo + 2, column = 8, padx = 5, pady = 5)
            self.barra_trafo_Secundario.insert(0,secundario)
            self.barra_trafo_Secundario.grid(row = trafo + 2, column = 9, padx = 5, pady = 5)

        self.t1 += 1
                             
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def create_entries_Gerador(self, size_Gerador = None, V_gerador = None, impedancia_pos = None, impedancia_neg = None, impedancia0 = None, ground_Gerador = None, con_Gerador = None, power_Generator = None, bus = None):

        self.save = False

        self.num_Gerador = Entry(self.framebox_Gerador)
        self.tensao_Gerador = Entry(self.framebox_Gerador)
        self.impedancia_pos_Gerador = Entry(self.framebox_Gerador)
        self.impedancia_neg_Gerador = Entry(self.framebox_Gerador)
        self.impedancia_z_Gerador = Entry(self.framebox_Gerador)
        self.ateramento_Gerador = Entry(self.framebox_Gerador)
        self.conexao_Gerador = Entry(self.framebox_Gerador)
        self.potencia_Gerador =  Entry(self.framebox_Gerador)
        self.barra_Gerador = Entry(self.framebox_Gerador)
        self.entradas_Gerador.append((self.tensao_Gerador))

        count4 = len(self.entradas_Gerador) + 1

        if size_Gerador is None:

            if self.load:
                self.num_Gerador.grid(row = count4, column = 0, padx = 5, pady = 5)
                self.num_Gerador.insert(END, self.g1-1)
                self.num_Gerador.config(state = 'readonly')
                self.tensao_Gerador.grid(row = count4, column = 1, padx = 5, pady = 5)
                self.impedancia_pos_Gerador.grid(row = count4, column = 2, padx = 5, pady = 5)
                self.impedancia_neg_Gerador.grid(row = count4, column = 3, padx = 5, pady = 5)
                self.impedancia_z_Gerador.grid(row = count4, column = 4, padx = 5, pady = 5)
                self.ateramento_Gerador.grid(row = count4, column = 5, padx = 5, pady = 5)
                self.conexao_Gerador.grid(row = count4, column = 6, padx = 5, pady = 5)
                self.potencia_Gerador.grid(row = count4, column = 7, padx = 5, pady = 5)
                self.barra_Gerador.grid(row = count4, column = 8, padx = 5, pady = 5)
            
            else:
                self.num_Gerador.grid(row = count4, column = 0, padx = 5, pady = 5)
                self.num_Gerador.insert(END, self.g1)
                self.num_Gerador.config(state = 'readonly')
                self.tensao_Gerador.grid(row = count4, column = 1, padx = 5, pady = 5)
                self.impedancia_pos_Gerador.grid(row = count4, column = 2, padx = 5, pady = 5)
                self.impedancia_neg_Gerador.grid(row = count4, column = 3, padx = 5, pady = 5)
                self.impedancia_z_Gerador.grid(row = count4, column = 4, padx = 5, pady = 5)
                self.ateramento_Gerador.grid(row = count4, column = 5, padx = 5, pady = 5)
                self.conexao_Gerador.grid(row = count4, column = 6, padx = 5, pady = 5)
                self.potencia_Gerador.grid(row = count4, column = 7, padx = 5, pady = 5)
                self.barra_Gerador.grid(row = count4, column = 8, padx = 5, pady = 5)

        else:
            self.num_Gerador.grid(row = size_Gerador + 2, column = 0, padx = 5, pady = 5)
            self.num_Gerador.insert(END, size_Gerador + 1)
            self.num_Gerador.config(state = 'readonly')
            self.tensao_Gerador.insert(0, V_gerador)
            self.tensao_Gerador.grid(row = size_Gerador + 2, column = 1, padx = 5, pady = 5)
            self.impedancia_pos_Gerador.insert(0, impedancia_pos)
            self.impedancia_pos_Gerador.grid(row = size_Gerador + 2, column = 2, padx = 5, pady = 5)
            self.impedancia_neg_Gerador.insert(0, impedancia_neg)
            self.impedancia_neg_Gerador.grid(row = size_Gerador + 2, column = 3, padx = 5, pady = 5)
            self.impedancia_z_Gerador.insert(0, impedancia0)
            self.impedancia_z_Gerador.grid(row = size_Gerador + 2, column = 4, padx = 5, pady = 5)
            self.ateramento_Gerador.insert(0, ground_Gerador)
            self.ateramento_Gerador.grid(row = size_Gerador + 2, column = 5, padx = 5, pady = 5)
            self.conexao_Gerador.insert(0, con_Gerador)
            self.conexao_Gerador.grid(row = size_Gerador + 2, column = 6, padx = 5, pady = 5)
            self.potencia_Gerador.insert(0, power_Generator)
            self.potencia_Gerador.grid(row = size_Gerador + 2, column = 7, padx = 5, pady = 5)
            self.barra_Gerador.insert(0, bus)
            self.barra_Gerador.grid(row = size_Gerador + 2, column = 8, padx = 5, pady = 5)

        self.g1 += 1

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def create_entries_Linha(self, size_Linha = None, positiva = None, negativa = None, zero = None, height_Linha = None, primario_Linha = None, secundario_Linha = None):
        
        self.save = False

        self.num_Linha = Entry(self.framebox_Linha)
        self.impedancia_Positiva = Entry(self.framebox_Linha)
        self.impedancia_Negativa = Entry(self.framebox_Linha)
        self.impedancia_Zero = Entry(self.framebox_Linha)
        self.comprimento = Entry(self.framebox_Linha)
        self.barra_primario_Linha = Entry(self.framebox_Linha)
        self.barra_secundario_Linha = Entry(self.framebox_Linha)
        self.entradas_Linhas.append(self.impedancia_Positiva)

        count5 = len(self.entradas_Linhas) + 1

        if size_Linha is None:

            if self.load:
                self.num_Linha.grid(row = count5, column = 0, padx = 5, pady = 5)
                self.num_Linha.insert(END, self.l1 - 1)
                self.num_Linha.config(state = 'readonly')
                self.impedancia_Positiva.grid(row = count5, column = 1, padx = 5, pady = 5)
                self.impedancia_Negativa.grid(row = count5, column = 2, padx = 5, pady = 5)
                self.impedancia_Zero.grid(row = count5, column = 3, padx = 5, pady = 5)
                self.comprimento.grid(row = count5, column = 4, padx = 5, pady = 5)
                self.barra_primario_Linha.grid(row = count5, column = 5, padx = 5, pady = 5)
                self.barra_secundario_Linha.grid(row = count5, column = 6, padx = 5, pady = 5)

            else:
                self.num_Linha.grid(row = count5, column = 0, padx = 5, pady = 5)
                self.num_Linha.insert(END, self.l1)
                self.num_Linha.config(state = 'readonly')
                self.impedancia_Positiva.grid(row = count5, column = 1, padx = 5, pady = 5)
                self.impedancia_Negativa.grid(row = count5, column = 2, padx = 5, pady = 5)
                self.impedancia_Zero.grid(row = count5, column = 3, padx = 5, pady = 5)
                self.comprimento.grid(row = count5, column = 4, padx = 5, pady = 5)
                self.barra_primario_Linha.grid(row = count5, column = 5, padx = 5, pady = 5)
                self.barra_secundario_Linha.grid(row = count5, column = 6, padx = 5, pady = 5)

        else:
            self.num_Linha.grid(row = size_Linha + 2, column = 0, padx = 5, pady = 5)
            self.num_Linha.insert(END, size_Linha + 1)
            self.num_Linha.config(state = 'readonly')
            self.impedancia_Positiva.insert(0, positiva)
            self.impedancia_Positiva.grid(row = size_Linha + 2, column = 1, padx = 5, pady = 5)
            self.impedancia_Negativa.insert(0, negativa)
            self.impedancia_Negativa.grid(row = size_Linha + 2, column = 2, padx = 5, pady = 5)
            self.impedancia_Zero.insert(0, zero)
            self.impedancia_Zero.grid(row = size_Linha + 2, column = 3, padx = 5, pady = 5)
            self.comprimento.insert(0, height_Linha)
            self.comprimento.grid(row = size_Linha + 2, column = 4, padx = 5, pady = 5)
            self.barra_primario_Linha.insert(0, primario_Linha)
            self.barra_primario_Linha.grid(row = size_Linha + 2, column = 5, padx = 5, pady = 5)
            self.barra_secundario_Linha.insert(0, secundario_Linha)
            self.barra_secundario_Linha.grid(row = size_Linha + 2, column = 6, padx = 5, pady = 5)

        self.l1 += 1

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion = self.canvas.bbox('all'))

    def load_csv(self):

        self.load = True

        barra_ID = []
        tensao_Barra = []

        transformador_ID = []
        impedancia_Transformador = []
        aterramento_primario_Transformador = []
        aterramento_secundario_Transformador = []
        tensao_primario_Transformador = []
        tensao_secundario_Transformador = []
        potencia_Transformador = []
        conexao_Transformador = []
        barra_primario_Transformador = []
        barra_secundario_Transformador = []

        gerador_ID = []
        tensao_Gerador = []
        impedancia_positiva_Gerador = []
        impedancia_negativa_Gerador = []
        impedancia_zero_Gerador = []
        aterramento_Gerador = []
        conexao_Gerador = []
        potencia_Gerador = []
        barra_Gerador = []

        linha_ID = []
        impedancia_pos_Linha = []
        impedancia_neg_Linha = []
        impedancia_0_Linha = []
        comprimento = []
        barra_primario_Linha = []
        barra_secundario_Linha = []

        with open('Barra.csv', newline='') as barra:
            reader_Barra = csv.DictReader(barra)
            
            for b in reader_Barra:
                barra_ID.append(b['Barra'])
                tensao_Barra.append(b['Tensao'])

        size_Barra = len(barra_ID)

        for i in range(size_Barra):

            if self.barra.get() and self.tensao.get():
                self.bus.append(self.barra.get())
                self.voltage.append(self.tensao.get())

            self.create_entries_Barras(i, barra_ID[i],tensao_Barra[i])
    
        with open('Transformador.csv', newline='') as transformador:
            reader_Transformador = csv.DictReader(transformador)

            for t in reader_Transformador:
                transformador_ID.append(t['Transformador'])
                impedancia_Transformador.append(t['Impedancia_percentual'])
                aterramento_primario_Transformador.append(t['Impedancia_aterramento_primario'])
                aterramento_secundario_Transformador.append(t['Impedancia_aterramento_secundario'])
                tensao_primario_Transformador.append(t['Tensao primario'])
                tensao_secundario_Transformador.append(t['Tensao secundario'])
                potencia_Transformador.append(t['Potencia'])
                conexao_Transformador.append(t['Tipo_de_conexao'])
                barra_primario_Transformador.append(t['Conexao_primario'])
                barra_secundario_Transformador.append(t['Conexao_secundario'])

        for j in range(len(transformador_ID)):

            if self.num_Trafo.get() and self.impedancia_Percentual.get():

                self.transformer.append(self.num_Trafo.get())
                self.impedance_T.append(self.impedancia_Percentual.get())
                
                if self.aterramento_Primario.get():
                    self.ground_primary_T.append(self.aterramento_Primario.get())
                else:
                    self.ground_primary_T.append(0)

                if self.aterramento_Secundario.get():
                    self.ground_secondary_T.append(self.aterramento_Secundario.get())
                else:
                    self.ground_secondary_T.append(0)
                
                self.voltage_primary_T.append(self.tensao_Primario.get())
                self.voltage_secundary_T.append(self.tensao_Secundario.get())
                self.power_T.append(self.potencia_Trafo.get())
                self.type_con_T.append(self.conexao_Trafo.get())
                self.bus_primary_T.append(self.barra_trafo_Primario.get())
                self.bus_secondary_T.append(self.barra_trafo_Secundario.get())

            self.create_entries_Trafo(j, impedancia_Transformador[j], aterramento_primario_Transformador[j], aterramento_secundario_Transformador[j], tensao_primario_Transformador[j], tensao_secundario_Transformador[j], potencia_Transformador[j], conexao_Transformador[j], barra_primario_Transformador[j], barra_secundario_Transformador[j])

        with open('Gerador.csv', newline = '') as gerador:
            reader_Gerador = csv.DictReader(gerador)

            for g in reader_Gerador:
                gerador_ID.append(g['Gerador'])
                tensao_Gerador.append(g['Tensao'])
                impedancia_positiva_Gerador.append(g['Impedancia_positiva'])
                impedancia_negativa_Gerador.append(g['Impedancia_negativa'])
                impedancia_zero_Gerador.append(g['Impedancia_zero'])
                aterramento_Gerador.append(g['Impedancia_aterramento'])
                conexao_Gerador.append(g['Conexao_gerador'])
                potencia_Gerador.append(g['Potencia'])
                barra_Gerador.append(g['Barra_conexao'])
                
        for k in range(len(gerador_ID)):

            if self.num_Gerador.get() and self.tensao_Gerador.get():

                self.generator.append(self.num_Gerador.get())
                self.voltage_G.append(self.tensao_Gerador.get())
                self.impedance_pos_G.append(self.impedancia_pos_Gerador.get())
                self.impedance_neg_G.append(self.impedancia_neg_Gerador.get())
                self.impedance_0_G.append(self.impedancia_z_Gerador.get())
                self.ground_G.append(self.ateramento_Gerador.get())
                self.type_con_G.append(self.conexao_Gerador.get())
                self.power_G.append(self.potencia_Gerador.get())
                self.bus_G.append(self.barra_Gerador.get())

            self.create_entries_Gerador(k, tensao_Gerador [k], impedancia_positiva_Gerador[k], impedancia_negativa_Gerador[k], impedancia_zero_Gerador[k], aterramento_Gerador[k], conexao_Gerador[k], potencia_Gerador[k], barra_Gerador[k])

        with open('Linha.csv', newline = '') as linha:
            reader_Linha = csv.DictReader(linha)

            for l in reader_Linha:
                linha_ID.append(l['Linha'])
                impedancia_pos_Linha.append(l['Impedancia_positiva'])
                impedancia_neg_Linha.append(l['Impedancia_negativa'])
                impedancia_0_Linha.append(l['Impedancia_zero'])
                comprimento.append(l['Comprimento'])
                barra_primario_Linha.append(l['Primario'])
                barra_secundario_Linha.append(l['Secundario'])

        for x in range(len(linha_ID)):

            if self.num_Linha.get() and self.impedancia_Positiva.get():
                self.wire.append(self.num_Linha.get())
                self.impedance_pos_W.append(self.impedancia_Positiva.get())
                self.impedance_neg_W.append(self.impedancia_Negativa.get())
                self.impedance_0_W.append(self.impedancia_Zero.get())
                self.width_W.append(self.comprimento.get())
                self.bus_primary_W.append(self.barra_primario_Linha.get())
                self.bus_secondary_W.append(self.barra_secundario_Linha.get())

            self.create_entries_Linha(x, impedancia_pos_Linha[x], impedancia_neg_Linha[x], impedancia_0_Linha[x], comprimento[x], barra_primario_Linha[x], barra_secundario_Linha[x])
            

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))


root = Tk()
app = CSV_creator(master=root)
root.mainloop()