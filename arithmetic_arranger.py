def arithmetic_arranger(problems, statprint = False):
    # Aqui defino as variaveis para receber os valores a serem organizados.
    first = ''
    second = ''
    lines = ''
    sumx = ''
    
    # Essa condicional if limita a 5 o número de problemas, case tenha mais apresentará erro.
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Esse for usa o comando .split em cada problema para separar o primeiro do segundo número e do operador, atribuindo depois a firsts, seconds e operands, respectivamente. Apresenta mensagens de erro para diferentes problemas, soma ou subtrai dependedo do operador, formata as respostas nas variaveis criadas acima.
    for problem in problems:
        a = problem.split()
        firsts = a[0]
        seconds = a[2]
        operands = a[1]
        
        # Aqui usamos a condicional if para verificar se as variaveis firsts e seconds são números, caso não sejam retornará uma mesagem de erro.
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."

        # Essa condicional if checa o primeiro e segundo número se possuem mais de 4 digitos, caso possuam retornará uma mensagem de erro.
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."

        # Aqui verificamos se o operador é + ou -, somamos, subtraimos e formatamos os valores caso sejam., e retorna uma mensagem de erro caso não sejam.
        if (operands == '+' or operands == '-'):
          #Aqui caso o operador seja + atribuimos à variavel sums o valor da soma ou caso seja - atribuimos a subtração dos valores em firsts e seconds.
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))

            # Essa parte do código cria variavéis para formatarmos a apresentação dos problemas. Estamos usando length para receber armazenar o valor necessário de traços abaixo dos valores. top estamos usando para apresentar o valor de firsts e justificar a direita com base no tamanho de length. bottom coloca o operador ao lado de seconds e justifica seconds com base em length -1 (precisamos do -1 pois o operador ocupa um dos espaços disponíveis e sem isso ficaria um número para fora). em line atribuimos uma linha vazia pois usaremos essa variavel para receber os traços abaixo dos números. Por fim criamos res para apresentar a variavel sums com a soma ou subtração de firsts e seconds, justificamos para a direita com base em lenght. 
            length = max(len(firsts), len(seconds)) + 2
            top = str(firsts).rjust(length)
            bottom = operands + str(seconds).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)

            # Com esse for acrescentamos um traço com base no tamanho armazenado em length, se for 4, 4 traços, se for 5 será 5 traços.
            for l in range(length):
                line += '-'
            
            # Aqui a condicional if verifica enquanto o for roda se tem mais problemas e os formata. Caso tenha acrescenta espaços após os valores e caso não tenha deixa de acrescentar. 
            if problem != problems[-1]:
              first += top + '    '
              second += bottom + '    '
              lines += line + '    '
              sumx += res + '    '
            else:
              first += top
              second += bottom
              lines += line
              sumx += res
        
        # Aqui retornamos a mensagem de erro caso os operadores não sejam + ou -.
        else:
            return "Error: Operator must be '+' or '-'."

    # Essa condicional if verifica se statprint é True, caso seja formatará sumx para aparecer no final De arranged_problems e organiza arrenged_problems para aparecer first uma quebra de linha então second, uma nova quebra de linha e lines.
    if statprint:
        sumx.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
        return arranged_problems

    return arranged_problems