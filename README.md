# Tasks-Automation
 Automatizando tarefas com linguagem Python / Automating tasks with Python language.


## Instruções importantes
 Antes de executar o programa, é necessário primeiro certificar-se de que as bibliotecas necessárias estão instaladas. Se não estiverem, abra o terminal do seu computador ou o terminal do VS Code e digite o comando pip install pyautogui.

 1. Se o comando pip não for reconhecido, abra o Python IDLE, abra em arquivos, selecione abrir arquivo, procure a pasta Script e copie seu endereço.
 2. Abra documentos em seu desktop, clique em 'Este Computador', pressione o botão direito de seu mouse e clique em 'Propriedades' para abrir a interface do Sistema.
 3. Procure o menu de 'Configurações avançadas' e clique-o, abrindo o menu, clique em 'Variáveis de ambiente', selecione a variável Path, clique em 'Editar' e cole o endereço da pasta Script em uma das linhas. Resolvido!

Para implementar este sistema sem erros, você precisará abrir a ferramenta 'mouseInfo', abra o terminal de seu computador ou o do VS Code e digite python, em seguida faça a importação do mouseInfo digitando 'from mouseinfo import mouseInfo', depois da importação, no mesmo terminal digite mouseInfo() para chamar o método. Pronto! Você já tem a ferramenta para te auxiliar matematicamente nas coordenadas de seu mouse. À medida que você vai arrastando o seu mouse, a ferramenta vai calculando a posição do cursor.

Observe que, na interface do mouseInfo, há uma folha de registros em branco personalizada, nela é possível listar e apagar os registros das coordenadas. Mova o seu mouse em direção aos pontos e pressione 'F6' em cada um dos pontos, para registrar as coordenadas e as incluir no programa python. Isto irá determinar o que a máquina irá fazer de modo a cumprir a essa tarefa, do início ao fim de acordo com a sua folha de código. Bons estudos!

Importante: Baixe todos os arquivos! Aviso! Estabeleça as coordenadas com eficiência, pois quando o programa for executado, você não poderá controlar o seu mouse até que o programa termine de ser executado. Para testes mais eficientes, chame o método sleep() em cada linha depois do método click(), e dentro dos parênteses, defina o número de segundos para que a automação seja pausada liberando o controle temporário do seu mouse de acordo com o valor definido. Assim você terá tempo suficiente para cancelar a execução do programa, dependendo de quantos segundos você definir.


## Important instructions
 Before running the program, you must first make sure that the libraries are installed. If not, open your computer's terminal or VS Code terminal and type the command pip install pyautogui.

 1. If the pip command is not recognized, open Python IDLE, open in files, select open file, look for a Script folder and copy its address.
 2. Open documents on your desktop, click 'This Computer', press the right mouse button and click 'Properties' to open the System interface.
 3. Look for the 'Advanced Settings' menu and click it, opening the menu, click on 'Environment Variables', select the Path variable, click on 'Edit' and paste the Script folder address in one of the lines. Sorted out!

To implement this system without errors, you will need to open the 'mouseInfo' tool, open your computer's terminal or VS Code and type python, then import mouseInfo by typing 'from mouseinfo import mouseInfo', after importing, in the same terminal type mouseInfo() to call the method. Ready! You already have the tool to help you mathematically with the coordinates of your mouse. As you drag your mouse, the tool calculates the position of the cursor.

Note that, in the mouseInfo interface, there is a personalized blank record sheet, where you can list and delete coordinate records. Move your mouse towards the points and press 'F6' at each point to record the coordinates and include them in the python program. This will determine what the machine will do to accomplish that task, from start to finish according to its code sheet. Happy studying!

Important: Download all files! Warning! Establish the coordinates efficiently because once the program runs, you will not be able to control your mouse until the program finishes running. For more efficient tests, call the sleep() method on each line after the click() method, and within the parentheses, define the number of seconds for the automation to be paused, releasing temporary control of your mouse according to the defined value . This way you will have enough time to cancel the program execution, depending on how many seconds you set.
