import sys
import re



def representsNumber(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False


def readHeader(line):

    """
    Retira informacao sobre o cabecalho do ficheiro CSV

    Args:
        line: primeira linha do ficheiro CSV

    Returns:
		headerList: lista de tupulos com quatro informacoes sobre cada coluna:
              ->  nome da coluna;
              ->  posicao em que termina a lista (lista de tamanho fixo) ou 
                    posicao a partir da qual a lista pode acabar (lista de tamanho variavel);
              ->  posicao em que termina a lista (lista de tamanho variavel);
              ->  funcao de agregacao a aplicar (lista);

    """

    posMax = -1
    posMin = -1

    headerList = []

    headerLine = re.findall(r'([^{,]+{\d+}(?:::\w+)?|[^{,]+{\d+,\d+}(?:::\w+)?|[^{,]*)[\n,]',line)

    for token in headerLine:
        m = re.match(r'(?P<value>[^{,]*)({(?P<dig1>\d+)(,(?P<dig2>\d+))?}(::(?P<op>\w+))?)?', token)
        
        if m.group('value') is not None and len(m.group('value')) > 0:
            value = m.group('value')
            op = 'default'

            if m.group('dig1') is not None:
                dig1 = int(m.group('dig1'))
                if m.group('dig2') is not None:
                    dig2 = int(m.group('dig2'))
                    posMin = posMax + dig1
                    posMax = posMax + dig2
                else:
                    posMax = posMax + dig1
                    posMin = posMax
                if m.group('op') is not None:
                    op = m.group('op')
            else:
                posMax += 1
                posMin = posMax

            headerList.append( (value,posMin,posMax,op) )

    return headerList


def readData(docLine, headerList):

    """
    Retira informacao sobre uma linha do ficheiro CSV

    Args:
        docLine: linha do ficheiro CSV para ser interpretada
        headerList: lista de tupulos com quatro informacoes sobre cada coluna

    Returns:
		parameterDict: dicionario com a informacao util retirada da linha fornecida

    """

    line = re.sub(r'\n', r'',docLine)

    splited = re.split(r',',line)

    parameterDict = dict()

    i = 0
    for value in headerList:
        buffer = []
        if i == value[2]:
            parameterDict[f"{value[0]}"] = splited[i]
            i += 1
        else:
            for pos in range (i, value[2] + 1):
                if (pos < value[1]):
                    buffer.append(splited[pos])
                else:
                    if splited[pos] != "":
                        buffer.append(splited[pos])
            i = value[2] + 1

            if value[3] == 'count' or value[3] == 'conta':
                total = len(buffer)
                parameterDict[f"{value[0] + '_' + value[3]}"] = total
            elif value[3] != 'default':
                allNumeric = True
                for b in buffer:
                    if not representsNumber(b):
                        allNumeric = False

                if allNumeric:
                    mapBuffer = map(int,buffer)

                    if value[3] == 'max':
                        total = max(buffer)
                    elif value[3] == 'min':
                        total = min(buffer)
                    elif value[3] == 'sum' or value[3] == 'soma':
                        total = sum(mapBuffer)
                    elif value[3] == 'avg' or value[3] == 'media':
                        total = sum(mapBuffer)/float(len(buffer))
                    else:
                        total = -1

                    parameterDict[f"{value[0] + '_' + value[3]}"] = total

                else:
                    parameterDict[f"{value[0]}"] = buffer

            else:
                parameterDict[f"{value[0]}"] = buffer

    return parameterDict


def writeData(file):

    """
    Recebe um ficheiro CSV e cria o ficheiro JSON correspondente

    Args:
        file: ficheiro CSV

    Returns:
		True: caso em que a funcao acaba corretamente

    """

    newFilename = re.sub(r".csv", ".json", file.name)
    fOut = open(newFilename, "w", encoding="utf-8")
    
    fOut.write("[\n")
    first = True
    headerList = readHeader(file.readline())
    for line in file:
        if not first:
            fOut.write(",\n")
        else:
            first = False
        exDict = readData(line, headerList)
        dictToFile(exDict,fOut)
    fOut.write("\n]")
    fOut.close()
    return True


def dictToFile(parameterDic, file):

    """
    Funcao auxiliar da writeData que a partir de um dicionario, escreve o seu conteudo em formato JSON no ficheiro fornecido

    Args:
        parameterDic: dicionario a ser escrito
        file: ficheiro a ser escrito

    Returns:

    """
    
    file.write("\t{\n")
    for i,(key, value) in enumerate(parameterDic.items()):
        
        if type(value) is not list:
            if representsNumber(value):
                file.write(f'\t\t\"{key}\": {value}')
            else:
                file.write(f'\t\t\"{key}\": \"{value}\"')
        else:
            #Ver se os elementos podem ser todos convertidos para inteiros
            allNumeric = True
            for v in value:
                if not representsNumber(v):
                    allNumeric = False
            #Se todos forem númericos, eliminamos os espaços e as '
            if allNumeric:
                text = re.sub(r"[ ']", "", str(value))
            else: #Senão eliminamos os espaços e transformamos as ' em "
                text2 = re.sub(r" +", "", str(value))
                text = re.sub(r"'","\"", text2)
            
            file.write(f'\t\t\"{key}\": {text}')
            
        if i == len(parameterDic.items()) - 1:
            file.write('\n')
        else:
            file.write(',\n')
    file.write("\t}")



file = None

while file is None:
    filename = input("Introduza o nome do ficheiro csv: ")
    
    if filename == "": 
        filename = "teste1.csv"
    
    try:
        file = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERRO! Ficheiro nao existe")
        continue

if writeData(file):
    print("SUCESSO! O ficheiro " + filename[:-4] + ".json criado com sucesso.")

file.close()
