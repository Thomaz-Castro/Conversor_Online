from random import randrange, randint
from unidecode import unidecode
import re


def InfFor_C(string):
    padrao = r'for\s*\(\s*([a-zA-Z0-9_]+)\s*=\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^)]+)\s*\)'
    match = re.search(padrao, string)
    if match:
        variavel = match.group(1)
        atribuicao = match.group(2)
        condicao = match.group(3)
        iteracao = match.group(4)
       
        return variavel, atribuicao, condicao, iteracao
    else:
        return None
    

def Indent_stripList(my_list):
    lista = my_list
    qtd = 0
    tab = "    "
    stri = ""
    for i, its in enumerate(lista):
        if (qtd != 0 and not (("}" in its and "{" not in its))):
            stri = str((tab*qtd) + its)
            lista[i] = stri
        if("{" in its and "}" not in its):
            qtd += 1
        if("}" in its and "{" not in its):
            qtd -= 1
            stri = str((tab*qtd) + its)
            lista[i] = stri
    
    return lista

        

def InfVetor_visualg (lin):
    txt = ""
    lin = lin.split("vetor")
    lin[1] = lin[1].split("]")
    del lin[0]
    del lin[0][1]
    txt = lin[0][0].strip()
    if ("," in txt):
        Vsplit = txt.split(",")
        Vsplit[0],Vsplit[1] = Vsplit[0].strip(),Vsplit[1].strip()
        Espc1 = Vsplit[0][(Vsplit[0].find("..")+2)]

        if ((Vsplit[0].find("..")+2) != (len(Vsplit[0])-1)):
            Espc1 = Espc1 + Vsplit[0][(Vsplit[0].find("..")+3)]
        Espc2 = Vsplit[1][(Vsplit[1].find("..")+2)]

        if ((Vsplit[1].find("..")+2) != (len(Vsplit[1])-1)):
            Espc2 = Espc2 + Vsplit[1][(Vsplit[1].find("..")+3)]

        value = str(Espc1)+"X"+str(Espc2)
    else:
        Espc = txt[(txt.find("..")+2)]
        if ((txt.find("..")+2) != (len(txt)-1)):
            Espc = Espc + txt[(txt.find("..")+3)]
        value = str(Espc)

    return value


def InfPara_visualg(string):
    string = string.lower().strip()
    padrao = r'para\s+(.*?)\s+de\s+(.*?)\s+ate\s+(.*?)(?:\s+passo\s+(.*?))?\s+faca'
    match = re.search(padrao, string)
    if match:
        grupos = match.groups()
        grupo4 = grupos[3] if grupos[3] else '1'
        grupos = grupos[:3] + (grupo4,) + grupos[4:]
        grupos = list(grupos)
        return grupos
    else:
        return None


def ate_dW(string):

    if (("(" in string) and (")" in string)):
        pilha = []
        conteudo = []
        for i, char in enumerate(string):
            
            if char == '(':
                pilha.append(i)
            elif char == ')':
                if pilha:
                    inicio = pilha.pop()
                    if not pilha:
                        conteudo.append(string[inicio+1:i])
                        
                else:
                    raise ValueError("Erro de correspondência de parênteses.")
        
        conteudo_parenteses = ", ".join(conteudo)
        conteudo_parenteses = "(" + conteudo_parenteses + ")"
        

        conteudo_parenteses = conteudo_parenteses.lower()
        conteudo_parenteses = conteudo_parenteses.replace(" e ", " && ")
        conteudo_parenteses = conteudo_parenteses.replace(" ou ", " || ")
        conteudo_parenteses = conteudo_parenteses.replace(" mod ", " % ")
        conteudo_parenteses = conteudo_parenteses.replace(" = ", " <>#3e3##fGG-- ")
        
        
        conteudo_parenteses = conteudo_parenteses.replace(" <> ", " == ")
        conteudo_parenteses = conteudo_parenteses.replace(" < ", " >=#3e3##fGG-- ")
        conteudo_parenteses = conteudo_parenteses.replace(" > ", " <=#3e3##fGG-- ")
        conteudo_parenteses = conteudo_parenteses.replace(" <= ", " >#3e3##fGG-- ")
        conteudo_parenteses = conteudo_parenteses.replace(" >= ", " <#3e3##fGG-- ")
        conteudo_parenteses = conteudo_parenteses.replace("#3e3##fGG--", "")
     

    else:
        conteudo_parenteses = "ERRO - parênteses não encontrados"

    return conteudo_parenteses

def Conditions_visualg(string):
    if (("(" in string) and (")" in string)):
        pilha = []
        conteudo = []
        for i, char in enumerate(string):
            if char == '(':
                pilha.append(i)
            elif char == ')':
                if pilha:
                    inicio = pilha.pop()
                    if not pilha:
                        conteudo.append(string[inicio+1:i])
                else:
                    raise ValueError("Erro de correspondência de parênteses.")

        conteudo_parenteses = ", ".join(conteudo)
        conteudo_parenteses = "(" + conteudo_parenteses + ")"
        conteudo_parenteses = conteudo_parenteses.lower()
        conteudo_parenteses = conteudo_parenteses.replace(" e ", " && ")
        conteudo_parenteses = conteudo_parenteses.replace(" ou ", " || ")
        conteudo_parenteses = conteudo_parenteses.replace(" mod ", " % ")
        conteudo_parenteses = conteudo_parenteses.replace(" = ", " == ")
        conteudo_parenteses = conteudo_parenteses.replace(" <> ", " != ")



    else:
        conteudo_parenteses = "ERRO - parênteses não encontrados"

    return conteudo_parenteses

def parent_printC(string):
    if (("(" in string) and (")" in string)):
        pilha = []
        conteudo = []
        for i, char in enumerate(string):
            if char == '(':
                pilha.append(i)
            elif char == ')':
                if pilha:
                    inicio = pilha.pop()
                    if not pilha:
                        conteudo.append(string[inicio+1:i])
                else:
                    raise ValueError("Erro de correspondência de parênteses.")

        conteudo_parenteses = ", ".join(conteudo)
        conteudo_parenteses = "(" + conteudo_parenteses + ")"
        conteudo_parenteses = conteudo_parenteses.lower()
    else:
        conteudo_parenteses = "ERRO - parênteses não encontrados"

    return conteudo_parenteses


def do_repita(string):
    if (("(" in string) and (")" in string)):
        pilha = []
        conteudo = []
        for i, char in enumerate(string):
            if char == '(':
                pilha.append(i)
            elif char == ')':
                if pilha:
                    inicio = pilha.pop()
                    if not pilha:
                        conteudo.append(string[inicio+1:i])
                else:
                    raise ValueError("Erro de correspondência de parênteses.")

        conteudo_parenteses = "".join(conteudo)
        conteudo_parenteses = str("(" + conteudo_parenteses + ")")
        conteudo_parenteses = conteudo_parenteses.lower()
        conteudo_parenteses = conteudo_parenteses.replace(" && ", " e ")
        conteudo_parenteses = conteudo_parenteses.replace(" || ", " ou ")
        conteudo_parenteses = conteudo_parenteses.replace(" == ", " <> ")
        conteudo_parenteses = conteudo_parenteses.replace(" >= ", " < ")
        conteudo_parenteses = conteudo_parenteses.replace(" <= ", " > ")
        conteudo_parenteses = conteudo_parenteses.replace(" > ", " <= ")
        conteudo_parenteses = conteudo_parenteses.replace(" < ", " >= ")
        conteudo_parenteses = conteudo_parenteses.replace("", "")

    else:
        conteudo_parenteses = "ERRO - parênteses não encontrados"

    return conteudo_parenteses

def Conditions_C(string):
    if (("(" in string) and (")" in string)):
        pilha = []
        conteudo = []
        for i, char in enumerate(string):
            if char == '(':
                pilha.append(i)
            elif char == ')':
                if pilha:
                    inicio = pilha.pop()
                    if not pilha:
                        conteudo.append(string[inicio+1:i])
                else:
                    raise ValueError("Erro de correspondência de parênteses.")

        conteudo_parenteses = ", ".join(conteudo)
        conteudo_parenteses = "(" + conteudo_parenteses + ")"
        conteudo_parenteses = conteudo_parenteses.lower()
        conteudo_parenteses = conteudo_parenteses.replace(" && ", " e ")
        conteudo_parenteses = conteudo_parenteses.replace(" || ", " ou ")
        conteudo_parenteses = conteudo_parenteses.replace(" == ", " = ")
    else:
        conteudo_parenteses = "ERRO - parênteses não encontrados"

    return conteudo_parenteses


def espcVetor_visualg(string):
    if (("[" in string) and ("]" in string)):
        pilha = []
        conteudo = []
        mpnt = {}
        for i, char in enumerate(string):
            if char == '[':
                pilha.append(i)
            elif char == ']':
                if pilha:
                    inicio = pilha.pop()
                    if not pilha:
                        conteudo.append(string[inicio+1:i])
                else:
                    raise ValueError("Erro de correspondência de chaves.")
                    
        lisa = conteudo.copy()
        for i , itens in enumerate(lisa):
            stri = str(itens)
            if (" " in stri):
                stri = stri.replace(" ","")
            lisa[i] = stri.replace(",","][")
            lisa[i] = "[" + lisa[i] + "]"

        for i, item in enumerate(conteudo):
            stri = str(item)
            conteudo[i] = ("[" + stri + "]")


        for i, item in enumerate(conteudo):
            mpnt[item] = lisa[i]
        
    else:
        mpnt = "xXx3 - ERRO"
        raise ValueError("Chaves não encontradas.") 
    
    return mpnt

def is_number(string):
    if string.startswith("-"):
        string = string[1:]
    return string.isnumeric()

def addVarName_DictList(lis, typ):
    varis = {}
    if typ == "f":
        for it in lis:
            var_name = str(it)
            varis[var_name] = r"%f" 
    if typ == "i":
        for it in lis:
            var_name = str(it)
            varis[var_name] = r"%d"  
    if typ == "s":
        for it in lis:
            var_name = str(it)
            varis[var_name] = r"%s"   
    
    return varis        

def extract_varName(string, typ):
    txt = str(string)
    vrs = []
    if "," not in txt:
        if typ == "f":
            txt = txt.replace("float ", "")
            txt = txt.replace(";", "")
        if typ == "i":
            txt = txt.replace("int ", "")
            txt = txt.replace(";", "")
        if typ == "s":
            txt = txt.replace("char ", "")
            txt = txt.replace("[100];", "")
        txt = txt.strip()
        vrs.append(txt)
    else:
        vrs = txt.strip(",").split(",")
        for i, it in enumerate(vrs):
            stri = str(it)
            if typ == "f":
                stri = stri.replace("float ", "")
                stri = stri.replace(";", "")
            if typ == "i":
                stri = stri.replace("int ", "")
                stri = stri.replace(";", "")
            if typ == "s":
                stri = stri.replace("char ", "")
                stri = stri.replace("[100];", "")
            if " " in stri:
                stri = stri.replace(" ", "")
            vrs = [stri if x == it else x for x in vrs]

    return vrs

def convEsc_forPrint(string:str, dic:dict):
    txt = string
    varis = dic
    txt = txt.replace("printf","")
    txt = txt.replace(");", "")
    txt = txt.strip()
    txt = txt[1:]
    vle = []
    ToF = False
    lax = ""
    lax2 = "" 
    lax3 = ""


    anls = txt.split('"')

    if len(anls) == 3 and anls[0] == "" and anls[2] == "":
        return string
    else:
        for i, txt in enumerate(anls):
            anls[i] = anls[i].strip()
            if i == 0:
                if len(anls[i]) > 0 and anls[i][len(anls[i]) - 1] == "," and anls[i].count(",") == 1:
                    lax = anls[i].replace(",", "")
                    lax = lax.strip()
                    if "[" in lax:
                        lax = lax.split("[")
                        lax3 = "[" + str(lax[1]) + "[" + str(lax[2])
                        lax = str(lax[0])
                        lax3 = lax + lax3
                        ToF = True
                    lax2 = varis[lax]
                    anls[i] = '"' + lax2
                    if ToF == False:
                        vle.append(lax)
                    else:
                        vle.append(lax3)
                        ToF = False
                else:
                    anls[0] = '"' + anls[0]
            elif i == len(anls) - 1:
                if len(anls[i]) > 0 and anls[i][0] == "," and anls[i].count(",") == 1:
                    lax = anls[i].replace(",", "")
                    lax = lax.strip()
                    if "[" in lax:
                        lax = lax.split("[")
                        lax3 = "[" + str(lax[1]) + "[" + str(lax[2])
                        lax = str(lax[0])
                        lax3 = lax + lax3
                        ToF = True
                    lax2 = varis[lax]
                    anls[i] = lax2 + '"'
                    if ToF == False:
                        vle.append(lax)
                    else:
                        vle.append(lax3)
                        ToF = False
                else:
                    anls[i] = anls[i] + '"'
            else:
                if len(anls[i]) > 0 and anls[i][len(anls[i]) - 1] == "," and anls[i].count(",") == 2 and anls[i][0] == ",":
                    lax = anls[i].replace(",", "")
                    lax = lax.strip()
                    if "[" in lax:
                        lax = lax.split("[")
                        lax3 = "[" + str(lax[1]) + "[" + str(lax[2])
                        lax = str(lax[0])
                        lax3 = lax + lax3
                        ToF = True
                    lax2 = varis[lax]
                    anls[i] = lax2
                    if ToF == False:
                        vle.append(lax)
                    else:
                        vle.append(lax3)
                        ToF = False


        lax = " ".join(anls)
        lax2 = ",".join(vle)
        lax2 = "," + lax2

        vle = "printf (" + lax + lax2 + ");"
        return vle 


def strBib_ADD(texto):
    lax2 = texto
    
    pattern = r"\(|\)|\s+e\s+|\s+ou\s+"

    # Executa a divisão usando o padrão de expressão regular
    resultado = re.split(pattern, texto)
    elementos_validos = []
    elmt_Trocados = []

    for tx in resultado:
        if ("=" in tx or "<>" in tx) and tx.count('"') >= 2:
            elementos_validos.append(tx)

    for tx in elementos_validos:
        if "=" in tx:
            lax = tx.replace("=", ",")
            lax = "(strcmp( " + lax + ") == 0)"
            elmt_Trocados.append(lax)

        else:
            lax = tx.replace("<>", ",")
            lax = "(strcmp( " + lax + ") == 1)"
            elmt_Trocados.append(lax)

    for p1, p2  in zip(elmt_Trocados, elementos_validos):
        lax2 = lax2.replace(p2,p1)

    return lax2

def visualg_to_c(code):
    
    textoPrimario = code
    splitTxt = textoPrimario.splitlines()
    C_codeSplit = []
    ale = 0
    ttttttttttttttttttttttttt = 0
    tttttttttt2 = 0
    lax = ""
    lax2 = ""
    lax3 = ""
    lax4 = ""
    varis = {}
    try:

        for i, line in enumerate(splitTxt):
            
            if (i == 0):
                C_codeSplit.append("//" + line)
                C_codeSplit.append("#include <stdio.h>")
            elif (i !=0):
                if line.strip() == "":
                    ale = randrange(1,10)
                    if (ale < 5):
                        C_codeSplit.append("")

                else:
                    line = line.strip()
                    if ((line[0] == "/") and (line[1] == "/")):
                        C_codeSplit.append(line)
                    else:
                        line = line.lower()

                        if ("raizq" in line):
                            line = line.replace("raizq","sqrt")
                            if tttttttttt2 == 0:
                                C_codeSplit.insert(1,"#include<math.h>")
                                tttttttttt2 += 1
                        if ("exp" in line):
                            line = line.replace("exp","pow")
                            if tttttttttt2 == 0:
                                C_codeSplit.insert(1,"#include<math.h>")
                                tttttttttt2 += 1


                        #if ("var" in unidecode(line.strip().lower())):
                        if ("inteiro" in line and not '"' in line):
                            if ("[" not in line):
                                line = line.strip()
                                lax = "int " + line.replace(":", ";")
                                lax = lax.replace("inteiro", "")
                                lax = lax.strip()
                                Dx = extract_varName(lax,'i')
                                Dx = addVarName_DictList(Dx, 'i')
                                for key, value in Dx.items():
                                    varis[key] = value
                                C_codeSplit.append(lax)
                                lax = ""
                            else:
                                rg = InfVetor_visualg(line)
                                if ("X" in rg):
                                    rg = rg.split("X")
                                    lax = line.split(":")
                                    lax2 = lax[0].strip()
                                    varis[lax2] = r"%d"
                                    lax2 = "int " + lax2 + "[" + rg[0] + "]"+"[" + rg[1] + "];"
                                    C_codeSplit.append(lax2)
                                    lax = ""
                                    lax2 = "" 
                                else:
                                    lax = line.split(":")
                                    lax2 = lax[0].strip()
                                    varis[lax2] = r"%d"
                                    lax2 = "int " + lax2 + "[" + rg + "];"
                                    C_codeSplit.append(lax2)
                                    lax = ""
                                    lax2 = ""
                                    
                        if ("real" in line and not '"' in line):
                            if ("[" not in line):
                                line = line.strip()
                                lax = "float " + line.replace(":", ";")
                                lax = lax.replace("real", "")
                                lax = lax.strip()
                                Dx = extract_varName(lax,'f')
                                Dx = addVarName_DictList(Dx, 'f')
                                for key, value in Dx.items():
                                    varis[key] = value
                                C_codeSplit.append(lax)
                                lax = ""
                            
                            else:
                                rg = InfVetor_visualg(line)
                                if ("X" in rg):
                                    rg = rg.split("X")
                                    lax = line.split(":")
                                    lax2 = lax[0].strip()
                                    varis[lax2] = r"%f"
                                    lax2 = "float " + lax2 + "[" + rg[0] + "]"+"[" + rg[1] + "];"
                                    C_codeSplit.append(lax2)
                                    lax = ""
                                    lax2 = "" 
                                else:
                                    lax = line.split(":")
                                    lax2 = lax[0].strip()
                                    varis[lax2] = r"%f"
                                    lax2 = "float " + lax2 + "[" + rg + "];"
                                    C_codeSplit.append(lax2)
                                    lax = ""
                                    lax2 = ""

                        if ("caractere" in line  and not '"' in line):
                            if ("[" not in line):
                                line = line.strip()
                                lax = "char " + line.replace(":", "[100];")
                                lax = lax.replace("caractere", "")
                                lax = lax.strip()
                                Dx = extract_varName(lax,'s')
                                Dx = addVarName_DictList(Dx, 's')
                                for key, value in Dx.items():
                                    varis[key] = value
                                C_codeSplit.append(lax)
                                lax = ""
                            
                            else:
                                rg = InfVetor_visualg(line)
                                lax = line.split(":")
                                lax2 = lax[0].strip()
                                varis[lax2] = r"%s"
                                lax2 = "char " + lax2 + "[100]"+"[" + rg + "];"
                                C_codeSplit.append(lax2)
                                lax = ""
                                lax2 = ""


                        if (("=" in line or "<>" in line) and line.count('"') >= 2):
                            lax = unidecode(line)
                            
                            lax2 = lax
                            if "enquanto" in lax:
                                lax = lax.replace("enquanto" , "")
                                lax = lax.replace("faca" , "")
                                typ = "enqt"
                            if "ate" in lax:
                                lax = lax.replace("ate", "")
                                if "<>" in lax:
                                    lax = lax.replace("<>", "=")
                                else:
                                    lax = lax.replace("=", "<>")
                                typ = "at"
                            if "entao" in lax:
                                lax = lax.replace("se", "")
                                lax = lax.replace("entao", "")
                                typ = "ent"
                            
                            lax = lax.strip()
                            if not "(" in lax and not ")" in lax:
                                lax = "(" + lax + ")"
                            
                            parent = strBib_ADD(lax)

                            raill = typ

                            if raill == "enqt":
                                lax = "enquanto " + parent + " faca"
                            elif raill == "at":
                                lax = "ate " + parent 
                            elif raill == "ent":
                                lax = "se " + parent + "entao"

                            line = lax
                            
                            if ttttttttttttttttttttttttt == 0:
                                C_codeSplit.insert(1, "#include<string.h>")
                                ttttttttttttttttttttttttt += 1





                        if ("inicio" in unidecode(line.strip().lower())):
                            ale = randrange(0,10)
                            if (ale%2==0):
                                C_codeSplit.append("")
                            C_codeSplit.append("int main(){")
                        if ("fimalgoritmo" in line):
                            C_codeSplit.append("}")
                        
                        if ("para" in line and "fimpara" not in line):
                            infs = InfPara_visualg(line)
                            if len(infs) != 0:
                                lax = str("for(" + infs[0] + " = ")
                                if is_number(infs[1]) == True and is_number(infs[2]) == True and is_number(infs[3]) == True:
                                    if ((int(infs[1])<int(infs[2])) and int(infs[3])>0):
                                        if infs[1] == "1":
                                            lax = lax + "0; " + infs[0] +  " < "+ infs[2] + "; "
                                        else:
                                            lax = lax + infs[1] +"; " + infs[0] + " <= "+ infs[2] + "; "
                                        if infs[3] == "1":
                                            lax = lax + infs[0] + "++){" 
                                        else:
                                            lax = lax + infs[0] + " += " + infs[3]+"){"
                                    else: 
                                        infs[3] = str(int(infs[3])*-1)
                                        lax = lax + infs[1] +"; " + infs[0] + " >= "+ infs[2] + "; "
                                        if infs[3] == "-1":
                                            lax = lax + infs[0] + "--){" 
                                        else:
                                            lax = lax + infs[0] + " -= " + infs[3]+"){"
                                else:
                                    if is_number(infs[3]):
                                        if int(infs[3])>0:
                                            lax = lax + infs[1] + "; " + infs[0] + " <= "+ infs[2] + "; "
                                            if infs[3] == "1":
                                                lax = lax + infs[0] + "++){" 
                                            else:
                                                lax = lax + infs[0] + " += " + infs[3]+"){"
                                        else:
                                            infs[3] = str(int(infs[3])*-1)
                                            lax = lax + infs[1] +"; " + infs[0] + " >= "+ infs[2] + "; "
                                            if infs[3] == "-1":
                                                lax = lax + infs[0] + "--){" 
                                            else:
                                                lax = lax + infs[0] + " -= " + infs[3]+"){"
                                    else:
                                        lax = lax + infs[1] + "; " + infs[0] + " <= "+ infs[2] + "; " + infs[0] + " += " + infs[3]+"){"
                                C_codeSplit.append(lax)
                                lax = ""
                            
                        if ("fimpara" in line):
                            C_codeSplit.append("}")
                        if ("enquanto" in line and "fim" not in line):
                            lax = line.replace("enquanto" , "")
                            lax = lax.replace("faca" , "")
                            lax = lax.strip()
                            if not "(" in lax and not ")" in lax:
                                lax = "(" + lax + ")"
                            parent = Conditions_visualg(lax)

                            if ("(" in parent):
                                C_codeSplit.append("while"+parent+"{")
                            else:
                                print("linha " + str(i+1) + ": ERRO, coloque a condição entre parentêses")
                                C_codeSplit.append("while( -ERRO CONDITION- ){")

                        if ("fimenquanto" in line):
                            C_codeSplit.append("}")
                        if ("repita" in line):
                            C_codeSplit.append("do{")
                        if ("ate" in unidecode(line) and "se" not in line and "para" not in line):
                            lax = unidecode(line)
                            lax = lax.replace("ate", "")
                            lax = lax.strip()
                            if not "(" in lax and not ")" in lax:
                                lax = "(" + lax + ")"
                           
                            parent = ate_dW(lax)
                            if ("(" in parent):
                                
                                C_codeSplit.append("}while"+parent+";")
                            else:
                                print("linha " + str(i+1) + ": ERRO, coloque a condição entre parentêses")
                                C_codeSplit.append("}while( -ERRO CONDITION- );")
                            

                        if ("se" in line and "entao" in unidecode(line) and not "senao" in unidecode(line)):
                            lax = unidecode(line)
                            lax = lax.replace("se", "")
                            lax = lax.replace("entao", "")
                            lax = lax.strip()
                            if not "(" in lax and not ")" in lax:
                                lax = "(" + lax + ")"

                            parent = Conditions_visualg(lax)
                            if ("(" in parent):
                                C_codeSplit.append("if"+parent+"{")
                            else:
                                print("linha " + str(i+1) + ": ERRO, coloque a condição entre parentêses")
                                C_codeSplit.append("if( -ERRO CONDITION- ){")
                        if("senao" in unidecode(line)):
                            if "entao" in unidecode(line):
                                lax =  unidecode(line).replace("senao", "")
                                lax = lax.replace("se", "")
                                lax = lax.replace("entao", "")
                                lax = lax.strip()
                                if not "(" in lax and not ")" in lax:
                                    lax = "(" + lax + ")"
                                parent = Conditions_visualg(lax)
                                if ("(" in parent):
                                    C_codeSplit.append("} else if "+parent+" {")

                            else:    
                                C_codeSplit.append("} else{")

                        if ("fimse" in line):
                            C_codeSplit.append("}")
                        if ("<-" in line or ":=" in line):
                            line = line.replace(":=","<-")
                            lax2 = line.split("<-")
                            lax3 = str(lax2[1])
                            lax2 = str(lax2[0])
                            lax2 = lax2.strip()
                            lax4 = varis[lax2]
                            if "s" in lax4 or "c" in lax4:
                                lax = "strcpy("+ lax2 + ", " + lax3 + ");"
                                if ttttttttttttttttttttttttt == 0:
                                    C_codeSplit.insert(1, "#include<string.h>")
                                    ttttttttttttttttttttttttt += 1
                                C_codeSplit.append(lax)
                                lax = ""
                            else:
                                lax = line
                                if ("[" in line and "]" in line):
                                    keys = espcVetor_visualg(line)
                                    for k, v in keys.items():
                                        kKey = str(k)
                                        vVal = str(v)
                                        if kKey in lax:
                                            lax = lax.replace(kKey, vVal)
                                lax = lax.replace("<-","=")
                                lax  = lax + ";"
                                C_codeSplit.append(lax)
                                lax = ""
                        if("escreva" in line and "escreval" not in line):
                            lax = line
                            if ("[" in line and "]" in line):
                                keys = espcVetor_visualg(line)
                                for k, v in keys.items():
                                    kKey = str(k)
                                    vVal = str(v)
                                    if kKey in lax:
                                        lax = lax.replace(kKey, vVal)
                            lax = lax.replace("escreva", "printf")
                            lax = lax +";"
                            lax = convEsc_forPrint(lax, varis)
                            C_codeSplit.append(lax)
                            lax = ""
                        if("escreval" in line):
                            lax3 = False
                            lax = line.replace(")","")
                            lax = lax.rstrip()
                            lax = lax + ")"
                            if "()" in lax:
                                lax3 = True


                            if lax3 == False:
                                lax = line
                                if ("[" in line and "]" in line):
                                    lax = line
                                if ("[" in line and "]" in line):
                                    keys = espcVetor_visualg(line)
                                    for k, v in keys.items():
                                        kKey = str(k)
                                        vVal = str(v)
                                        if kKey in lax:
                                            lax = lax.replace(kKey, vVal)
                                lax = lax.replace("escreval", "printf")
                                lax = lax +";"
                                lax = convEsc_forPrint(lax, varis)
                                indice = lax.rfind('"')
                                if indice != -1:
                                    lax = lax[:indice] + r'\n"' + lax[indice+1:]
                                lax = lax.replace('(" ', '("')
                                C_codeSplit.append(lax)
                                lax = ""
                            else:
                                C_codeSplit.append(r'printf ("\n");')
                        if ("leia" in line and ")" in line):
                            lax = line
                            if ("[" in line and "]" in line):
                                keys = espcVetor_visualg(line)
                                for k, v in keys.items():
                                    kKey = str(k)
                                    vVal = str(v)
                                    if kKey in lax:
                                        lax = lax.replace(kKey, vVal)
                            parent = Conditions_visualg(lax)
                            parent = parent.replace("(","")
                            parent = parent.replace(")","")
                            parent2 = parent.split("[", 1)[0].strip()
                            lax  = r'scanf("'+ varis[str(parent2)] +r'",&'+parent+");"
                            C_codeSplit.append(lax)
                            lax = ""
                        if ("interrompa" in line):
                            C_codeSplit.append("break;")
                            
        
        C_codeSplit = Indent_stripList(C_codeSplit)
        c_code = "\n".join(C_codeSplit)          
        return c_code
    except Exception as erro:
        print("Seu Código em visualg possui algum erro de Sintaxe, verifique-o, tente tambem colocar suas condições entre parentêses")
        return ("Seu Código em visualg possui algum erro de Sintaxe, verifique-o, tente tambem colocar suas condições entre parentêses")

def espcVetor_C(string, tipe):
    if tipe != "caractere":
        dcl = string.split(",")
        rtn = [[],[]]
        lax = ""
        if len(dcl) == 1:
            padrao = r'\[[^\]]+\]'
            resultado = re.findall(padrao, string)
            
            tamanhos = []
            for tamanho in resultado:
                tamanho = tamanho.strip('[]')
                tamanhos.append(tamanho)
            
            return tamanhos
        else:
            
            for i, item in enumerate(dcl):
                if "[" in item:
                    padrao = r'\[[^\]]+\]'
                    resultado = re.findall(padrao, item)
                    
                    tamanhos = []
                    for tamanho in resultado:
                        tamanho = tamanho.strip('[]')
                        tamanhos.append(tamanho)
                    
                    if len(tamanhos) == 1:
                        spt = item.split("[")
                        spt = str(spt[0].strip())
                        lax = spt + ": vetor [1.." + tamanhos[0] + "] de " + tipe 
                        rtn[1].append(lax)
                        lax = ""

                    elif len(tamanhos) == 2:
                        spt = item.split("[")
                        spt = str(spt[0].strip())
                        lax = spt + ": vetor [1.." + tamanhos[0] + ",1.." + tamanhos[1] +"] de " + tipe 
                        rtn[1].append(lax)
                        lax = ""
                    
                else:
                    rtn[0].append(item)
            
            if len(rtn[0]) != 0:      
                lax = ", ".join(rtn[0])
                lax = lax + ": " + tipe
                rtn[0].clear()
                rtn[0].append(lax)

            return rtn
    else:
        dcl = string.split(",")
        rtn = [[],[]]
        lax = ""
        if len(dcl) == 1:
            padrao = r'\[[^\]]+\]'
            resultado = re.findall(padrao, string)
            if resultado != []:
                item = dcl[0]
                tamanhos = []
                for tamanho in resultado:
                    tamanho = tamanho.strip('[]')
                    tamanhos.append(tamanho)

                if len(tamanhos) == 1:
                    spt = item.split("[")
                    spt = str(spt[0].strip())
                    lax = spt + ": caractere"
                    rtn[0].append(lax)
                    lax = ""

                elif len(tamanhos) == 2:
                    spt = item.split("[")
                    spt = str(spt[0].strip())
                    lax = spt + ": vetor [1.." + tamanhos[0] + ",1.." + tamanhos[1] +"] de " + tipe 
                    rtn[0].append(lax)
                    lax = ""
            else:
                spt = dcl[0].strip()
                lax = spt + "+ caractere"
                rtn[0].append(lax)
            
        else:
            
            for i, item in enumerate(dcl):
                if "[" in item:
                    padrao = r'\[[^\]]+\]'
                    resultado = re.findall(padrao, item)
                    
                    tamanhos = []
                    for tamanho in resultado:
                        tamanho = tamanho.strip('[]')
                        tamanhos.append(tamanho)
                    
                    if len(tamanhos) == 1:
                        spt = item.split("[")
                        spt = str(spt[0].strip())
                        lax = spt + ": vetor [1.." + tamanhos[0] + "] de " + tipe 
                        rtn[1].append(lax)
                        lax = ""

                    elif len(tamanhos) == 2:
                        spt = item.split("[")
                        spt = str(spt[0].strip())
                        lax = spt + ": vetor [1.." + tamanhos[0] + ",1.." + tamanhos[1] +"] de " + tipe 
                        rtn[1].append(lax)
                        lax = ""
                    
                else:
                    rtn[0].append(item)
            
            if len(rtn[0]) != 0:      
                lax = ", ".join(rtn[0])
                lax = lax + ": " + tipe
                rtn[0].clear()
                rtn[0].append(lax)

        return rtn
    
def substituir_virgula(texto):
    novo_texto = ""
    dentro_parenteses = False

    for caractere in texto:
        if caractere == "(":
            dentro_parenteses = True
        elif caractere == ")":
            dentro_parenteses = False

        if dentro_parenteses and caractere == ",":
            novo_texto += caractere
        elif not dentro_parenteses and caractere == ",":
            novo_texto += "---X3X3x3,,,,,,,    ---"
        else:
            novo_texto += caractere

    return novo_texto

def substituir_marcacoes(texto):
    txt = texto.lstrip('"')
    txt = txt.split('"')
    lax = str(txt[0])
    txt = str(txt[1])
    txt = txt.lstrip(",")
    txt = txt.strip()
    txt = substituir_virgula(txt)
    palavras = txt.split("---X3X3x3,,,,,,,    ---")

    for i, nm in enumerate(palavras):
        palavras[i] = nm.strip()

    lax = '"' + lax


    padrao = r'%[a-zA-Z]+'
    correspondencias = re.findall(padrao, lax)

    for marca, palavra in zip(correspondencias, palavras):
        lax = lax.replace(marca, f'", {palavra}, "', 1)

    return lax


def possui_porcentagem_letra(string):
    padrao = r"%[a-zA-Z]"
    correspondencia = re.search(padrao, string)
    if correspondencia:
        return True
    else:
        return False

def sep_Bn (string):
    if string.strip('"').strip() == "\\n":
        return ["escreval()"]
    else:

        linhas = []
        l2 = []

        lax = string.split("\\n")
        
        """ for linha in lax:
            linha = linha.strip('"')
            if linha != "":
                linha = '"' + linha + '"'
                l2.append(linha) """


        if len(lax) == 2:
            if lax[0] == '"' and lax[1] == '"':
                linhas.append(("escreval()"))
            elif len(lax[0])>1 and lax[1] == '"':
                lax.pop(1)

        

        if len(linhas) != 2:
            for linha in lax:
                linha = linha.strip('"')
                linha = '"' + linha + '"'

                if linha.strip('"') == "" or linha == "":
                    linhas.append(("escreval()"))
                else:
                    linhas.append(("escreval(" + linha + ")"))

        return linhas


def correct_aps(string):
    lax = string
    lax2 = lax
    if string.endswith('")'):
        lax =  string.replace('")', "")
        lax = lax.strip()
        if lax.endswith(","):
            lax = lax.rstrip(",")
            lax = lax + ")"
        else:
            lax = lax + ' ")'

    lax2 = lax

    if lax2.startswith("escreval"):
        lax2 = lax2.replace("escreval", "")
        lax2 = lax2.strip()
        if lax2.startswith('(",'):
            lax2 = lax2.replace('(",', "(")
        lax2 = "escreval" + lax2
    else:
        lax2 = lax2.replace("escreva", "")
        lax2 = lax2.strip()
        if lax2.startswith('(",'):
            lax2 = lax2.replace('(",', "(")
        lax2 = "escreva" + lax2


    return lax2


def Indent_stripList_CtoVG(my_list):
    lista = my_list
    qtd = 0
    tab = "    "
    stri = ""
    for i, its in enumerate(lista):
        if not "inicio" in its:
            if "senao" in its:
                stri = str((tab*(qtd-1)) + its)
                lista[i] = stri
            else:
                if (qtd != 0 and not (("}" in its and "{" not in its))):
                    stri = str((tab*qtd) + its)
                    lista[i] = stri
                if ("faca" in its or "var" in its or "entao" in its or "repita" in its):
                    qtd += 1
                if ("fim" in its):
                    qtd -= 1
                    stri = str((tab*qtd) + its)
                    lista[i] = stri
                if ("ate" in its and not "para" in its):
                    qtd -= 1
                    stri = str((tab*qtd) + its)
                    lista[i] = stri
    
    return lista

def adicionar_chave(texto):
    linhas = texto.split("\n")
    novo_texto = []
    procurando = False
    vzs = 0

    for linha in linhas:
        if procurando:
            if linha.strip() == "}":
                novo_texto.append("}")
                for i in range (1, vzs+2):
                    novo_texto.append("}")
                novo_texto.append("")
                procurando = False
                vzs = 0
            else:
                novo_texto.append(linha)
        else:
            novo_texto.append(linha)

        if "else if" in linha.lower():
            if procurando == True:
                vzs += 1
            else:
                procurando = True

    return "\n".join(novo_texto)

def cmp_PraViG(texto, versao = 0):
    lax4 = texto
    if versao == 0:
        padrao = r"\(?\s*strcmp\s*\((.*?)\)\s*==\s*(\d+)?"  

        troq = []

        txt_novo = []
        
        ocorrencias = re.finditer(padrao, texto)

        # Criar uma lista aninhada com os resultados e os índices
        resultado = [[match.group(1), match.group(2), (match.start(), match.end())] for match in ocorrencias]

        for i in range(len(resultado)):
            lax = resultado[i][0].strip().split(",")
            lax2 = lax[1].strip()
            lax = str(lax[0]).strip()
            if resultado[i][1] == "0":
                lax3 =  "(" + lax + " == " + lax2 + ")"
            else:
                lax3 = "(" + lax + " != " + lax2 + ")"

            troq.append(lax3)

        
            itrable = 0
        
            for jkl in resultado:
                t_Range = list(range(jkl[2][0], jkl[2][1] + 1))
                difernss =  abs(abs(jkl[2][1] - jkl[2][0]) - len(troq[itrable])) + 1
            

                i = 0
                while i < len(lax4):
                
                    char = lax4[i]
                
                    if i == jkl[2][0]:
                        for char2 in troq[itrable]:
                            txt_novo.append(char2)
                        i = jkl[2][1]
                        for l in range(difernss):
                            txt_novo.append("¢")

                    else:
                        txt_novo.append(char) 
                    
                    i += 1
                
        
                lax4 = "".join(txt_novo)
                txt_novo=[]
            
                itrable += 1

            
            lax4 = lax4.replace("¢", " ")
            lax4 = re.sub(r'\s+', ' ', lax4)

            return lax4
    else:

        padrao = r"\((.*?)\)"

        troq = []
        txt_novo = []
        ocorrencias = re.finditer(padrao, texto)

        for ocorrencia in ocorrencias:
            item1, item2 = ocorrencia.group(1).split(",")
            troq.append((item1.strip(), item2.strip()))

        i1, i2 = troq[0][0], troq[0][1]
        lax2 = f"({i1} = {i2})"

        lax = lax4.split("=")
        lax = lax[0].strip()
        lax = f"se {lax2} entao\n     {lax} <- 0\nsenao\n    {lax} <- 1\nfimse"

        return lax

                   

def c_to_visualg(code):
    textoPrimario = code
    textoPrimario = adicionar_chave(textoPrimario)
    splitTxt = textoPrimario.splitlines()
    VG_codeSplit = []
    ale = 0
    lax = ""
    lax2 = ""
    lax3 = ""
    varis = {}
    ChOp = []

    for i, line in enumerate(splitTxt):
        if (i == 0):
            VG_codeSplit.append('algoritmo " programa Visualg "')
            VG_codeSplit.append('')
            VG_codeSplit.append('var')
            VG_codeSplit.append('')
        elif (i !=0):
            if line.strip() == "":
                ale = randrange(1,10)
                VG_codeSplit.append("")
                if (ale < 2):
                    VG_codeSplit.append("")

            else:
                line = line.strip()
                if ((line[0] == "/") and (line[1] == "/")):
                    VG_codeSplit.append(line)
                else:
                    line = line.lower()
                    if ("pow" in line):
                        line = line.replace("pow","exp")
                    if ("sqrt" in line):
                        line = line.replace("sqrt","raizq")
                    

                    if ("int " in line and '"' not in line and "{" not in line):
                        if ("[" not in line):
                            line = line.replace("int ", "")
                            line = line.replace(";", ": inteiro")
                            line = line.strip()
                            VG_codeSplit.append(line)
                        else:
                            line = line.replace("int ", "")
                            line = line.strip()
                            lax = espcVetor_C(line, "inteiro")
                            if len(lax[0]) == 0:
                                for i in lax[1]:
                                    VG_codeSplit.append(i)
                            else:
                                for i in range(0,2):
                                    for it in lax[i]:
                                        VG_codeSplit.append(it)


                    if ("float " in line):
                        if ("[" not in line and '"' not in line):
                            line = line.replace("float ", "")
                            line = line.replace(";", ": real")
                            line = line.strip()
                            VG_codeSplit.append(line)
                        else:
                            line = line.replace("float", "")
                            line = line.strip()
                            lax = espcVetor_C(line, "real")
                            if len(lax[0]) == 0:
                                for i in lax[1]:
                                    VG_codeSplit.append(i)
                            else:
                                for i in range(0,2):
                                    for it in lax[i]:
                                        VG_codeSplit.append(it)
                    if "char " in line:
                        line = line.replace("char ", "")
                        line = line.replace(";", "")
                        line = line.strip()
                        lax = espcVetor_C(line, "caractere")

                        if not lax[0]:
                            for item in lax[1]:
                                item = item.strip()
                                VG_codeSplit.append()
                        else:
                            combined_list = lax[0] + lax[1]
                            for item in combined_list:
                                VG_codeSplit.append(item.strip())

                    if ("strcpy" in line):
                        lax = line.replace("strcpy", "")
                        lax = lax.replace(";","")
                        lax = lax.strip()
                        lax = lax.strip("()")
                        lax = lax.replace(",", "<-")
                        VG_codeSplit.append(lax)

                    if ("strcmp" in line):
                        if " = " in line and not "while" in line and not "if" in line:
                            parent = cmp_PraViG(line, 1)
                            line = ""
                            VG_codeSplit.append(parent)
                        else:
                            parent = cmp_PraViG(line)
                            line = parent

                    if ("main" in line and "{" in line and "(" in line):
                        VG_codeSplit.append("inicio")
                        ChOp.insert(0,'fimalgoritmo')

                    if ("for " in line ):
                        lax = InfFor_C(line)
                        if lax is not None and len(lax) >= 3 and "0" == lax[1] and "=" not in lax[2] and len(lax[2]) > 0 and is_number(str(lax[2][len(lax[2])-1])):
                                if "++" in line:
                                    lax2 = "para " + lax[0] + " de 1 ate " + str(lax[2][(len(lax[2])-1)]) + " faca"
                                elif "--" in line:
                                    lax2 = "para " + lax[0] + " de" + lax[1] +  " ate " + str(lax[2][(len(lax[2])-1)]) + " passo -1 faca"
                        else:
                            lax3 = None
                            if lax is not None and len(lax) >= 4:
                                if "=" in lax[2] and not "==" in lax[2]:
                                    lax3 = lax[2].split("=")
                                elif "==" in lax[2]:
                                    lax3 = lax[2].split("==")
                                elif "<" in lax[2]:
                                    lax3 = lax[2].split("<")
                                elif ">" in lax[2]:
                                    lax3 = lax[2].split(">")
                                
                                  
                                if lax3 is not None and len(lax3) >= 2:
                                    lax3 = str(lax3[1])
                                    lax3 = lax3.strip()
                                else:
                                    lax3 = ""  # Ou qualquer outro valor padrão desejado
                                    
                                lax2 = "para " + lax[0] + " de " + lax[1] + " ate " + lax3
                                
                                if "++" in lax[3]:
                                    lax2 = lax2 + " faca"
                                elif "--" in lax[3]:
                                    lax2 = lax2 + " passo -1 faca"
                                else:  
                                    lax3 = lax[3].split("=")
                                    lax3 = lax3[1].strip()
                                    lax2 = lax2 + " passo "+ lax3 + " faca"
                        
                        VG_codeSplit.append(lax2)
                        lax = lax2 = lax3 = ""
                        ChOp.insert(0,'fimpara')

                    if ("scanf" in line):
                        lax = line.split("&")
                        lax = str(lax[1])
                        lax = lax.replace(");", "")
                        lax = "leia(" + lax + ")"
                        lax = lax.strip()
                        VG_codeSplit.append(lax)
                        lax = ""


                    if ("while" in line and not "}" in line and not '"' in line):
                        lax = Conditions_C(line)
                        lax = "enquanto " + lax + "faca"
                        VG_codeSplit.append(lax)
                        ChOp.insert(0,"fimenquanto")
                        lax = ""

                    if ("printf" in line):
                        line = line.replace(";","")
                        lax = line.count(r"\n")
                        if lax == 0:
                            if possui_porcentagem_letra(line):
                                line = line.lstrip("printf")
                                line = line.strip()
                                line = line.strip("()")
                                lax  = substituir_marcacoes(line)
                                lax = "(" + lax + " ) "
                                lax = parent_printC(lax)
                                lax = lax.strip("()")
                                lax = sep_Bn(lax)
                                for lnhs in lax:
                                    lnhs = correct_aps(lnhs)
                                    VG_codeSplit.append(lnhs)
                                lax = str("")

                            else:
                                lax = parent_printC(line)
                                lax = "escreva" + lax
                                VG_codeSplit.append(lax)
                                lax = str("")

                        else:
                            if possui_porcentagem_letra(line):
                                line = line.lstrip("printf")
                                line = line.strip()
                                line = line.strip("()")
                                lax  = substituir_marcacoes(line)
                                lax = "(" + lax + " ) "
                                lax = parent_printC(lax)
                                lax = lax.strip("()")
                                lax = sep_Bn(lax)
                                for lnhs in lax:
                                    lnhs = correct_aps(lnhs)
                                    VG_codeSplit.append(lnhs)
                                lax = str("")

                            else:
                                lax = parent_printC(line)
                                lax = lax.strip("()")
                                lax = sep_Bn(lax)
                                for lnhs in lax:
                                    VG_codeSplit.append(lnhs)
                        
                    if ("do" in line and "{" in line):
                        VG_codeSplit.append("repita")

                    if ("while" in line and "}" in line):
                        lax = line.replace("while", "")
                        lax = lax.replace("}", "")
                        lax = lax.replace(";","")
                        lax = lax.strip()
                        lax = do_repita(lax)
                        lax = "ate " + lax 
                        VG_codeSplit.append(lax)

                    if (("++" in line or "--" in line ) and not "(" in line):
                        if ("++" in line):
                            lax = line.replace("++","")
                            lax = lax.replace(";","")
                            lax = lax.strip()
                            lax =  lax + " <- " + lax + " + 1"
                        else:
                            lax = line.replace("--","")
                            lax = lax.replace(";","")
                            lax = lax.strip()
                            lax =  lax + " <- " + lax + " - 1"
                        VG_codeSplit.append(lax)

                        
                    if ("=" in line and (not "for" in line and not "while" in line and not "if" in line)):
                        if ("[" in line and "]" in line):
                                line = line.replace("][",",")
                        lax = line.replace("=", "<-")
                        lax =  lax.replace(";","")
                        VG_codeSplit.append(lax)
                        
                    if ("break" in line):
                        VG_codeSplit.append("interrompa")

                    if ("}" in line and not "{" in line and not "while" in line):
                        print(ChOp)
                        VG_codeSplit.append(ChOp[0])
                        ChOp.pop(0)
                       
                    if ("if" in line):
                        ChOp.insert(0, "fimse")

                    if ("if" in line and not "else" in line):
                        lax = line.replace("if", "")
                        lax = lax.replace("{", "")
                        lax = lax.strip()
                        lax = Conditions_C(lax)
                        lax = "se " + lax + " entao"
                        VG_codeSplit.append(lax)
                    


                    if ("else" in line):
                        if not "if" in line:
                            VG_codeSplit.append("senao")
                      
                        else:
                            VG_codeSplit.append("senao")
                            lax = line.replace("if", "")
                            lax = lax.replace("else", "")
                            lax = lax.replace("{", "")
                            lax = lax.replace("}", "")
                            lax = lax.strip()
                            lax = Conditions_C(lax)
                            lax = "se " + lax + " entao"
                            VG_codeSplit.append(lax)
                           
                            




                    if ("int" in line):
                        pass
                    if ("int" in line):
                        pass
        

    
   
    visualg_code = Indent_stripList_CtoVG(VG_codeSplit)
    visualg_code = "\n".join(visualg_code)          
    
    return visualg_code
