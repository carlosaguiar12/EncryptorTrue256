<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="encryptortrue256">EncryptorTrue256</h1>
<h2 id="tópicos">Tópicos</h2>
<ol>
<li>
<p>Proposta</p>
</li>
<li>
<p>O que é Criptografia?</p>
</li>
<li>
<p>Instalação das ferramentas</p>
<pre><code>3.a. — Anaconda
    3.a.b. — Baixando e instalando o Anaconda
    3.a.c. — Criação e detalhes sobre ambientes virtuais
3.b. — Instalando a biblioteca Pycryptodome
</code></pre>
</li>
<li>
<p>AES e modo de operação CBC</p>
</li>
<li>
<p>Criador</p>
</li>
</ol>
<h2 id="proposta">1. Proposta</h2>
<p>O <strong>EncryptorTrue256</strong> tem o propósito de criar proteção do tipo <em>confidencialidade</em> sobre os dados.</p>
<blockquote>
<p>Trata-se de um <em>script</em> capaz de criptografar (e descriptografar) arquivos a 256 bits.</p>
</blockquote>
<blockquote>
<p>O projeto está em fase inicial. Funciona bem, mas ainda falta implementar contramedidas razoáveis a <em>Ataques de Canal Lateral (Side Channel Attacks)</em>.</p>
</blockquote>
<h2 id="o-que-é-criptografia">2. O que é Criptografia?</h2>
<p><strong>Criptografia é a prática de codificar e decodificar dados.</strong> Quando os dados são criptografados, é aplicado um algoritmo para codificá-los de modo que eles não tenham mais o formato original e, portanto, não possam ser lidos. Os dados só podem ser decodificados ao formato original com o uso de uma chave de decriptografia específica.<br>
<em>[Fonte: <a href="https://www.kaspersky.com.br/resource-center/definitions/encryption">Kaspersky</a>]</em></p>
<h2 id="instalação-das-ferramentas">3. Instalação das ferramentas</h2>
<h3 id="a.-anaconda">3.a. Anaconda</h3>
<p>O <em>Anaconda</em> é uma poderosa solução tecnológica para a Ciência de Dados e pode abranger as linguagens <em>Python</em> e <em>R</em>, contendo ferramentas potentes para a análise de dados.</p>
<p>Mas aqui a usaremos para criar e gerenciar <em>Ambientes virtuais</em> com praticidade (veja mais detalhes no subtópico <strong>3.a.c.</strong>).</p>
<h3 id="a.b.-instalando-o-anaconda">3.a.b. Instalando o Anaconda</h3>
<p>Visite o <a href="https://www.anaconda.com/products/individual#Downloads">site de download</a> e escolha o instalador que condiz com a sua máquina e sistema operacional e baixe-o. Também é relevante escolher a  versão do Python que você quer que seja padrão (recomenda-se a 3.x).</p>
<blockquote>
<p>Exemplo para leigos’: <em>"O meu computador é Windows, 64 Bits, então no site de download eu escolho o Instalador que se parece com isso</em> — <strong>Windows 64-Bit Graphical Installer (466 MB)</strong>".</p>
</blockquote>
<h3 id="a.c.-criação-e-detalhes-sobre-ambientes-virtuais">3.a.c. Criação e detalhes sobre ambientes virtuais</h3>
<blockquote>
<p>Ambientes Virtuais podem ser encarados como uma <em>“caixa”</em> onde código é executado. Por exemplo: suponha que você tem a versão padrão do Python instalada na sua máquina e quer testar novas bibliotecas, mas aí surgem alguns <em>problemas</em>, como:</p>
</blockquote>
<ul>
<li>
<p>A biblioteca que eu quero instalar funciona na versão 3.4 do Python, mas eu tenho apenas a versão 3.7 instalada. E agora? Tenho que desinstalar tudo para adicionar uma única biblioteca?</p>
</li>
<li>
<p>Eu quero criar um projeto novo, mas seria péssimo se as versões de uma mesma biblioteca colidissem entre si ou se houvesse alguma confusão no momento de importar os módulos, porque se existem dois módulos <em>Biblioteca V1.0</em> e <em>Biblioteca V4.6</em> pode acontecer o seguinte conflito:</p>
<blockquote>
<p>from Biblioteca.Classe import método<br>
método(parâmetro)<br>
…<br>
<strong>SyntaxError</strong></p>
</blockquote>
<blockquote>
<p>O erro de sintaxe acima pode ter ocorrido porque no ambiente e projeto em que você estava executando o código houve uma confusão entre as versões 1.0 e 4.6 instaladas no mesmo lugar que continham o mesmo <strong>método</strong> usado no exemplo acima, cada um implementado de uma forma diferente do outro. Você gostaria que a sintaxe da versão 4.6 fosse executada, mas isso não ocorreu.</p>
</blockquote>
</li>
</ul>
<p>Isso tudo pode ser facilmente resolvido usando <strong>Ambientes Virtuais</strong>, que contêm versões isoladas do Python. E então se algo não sair como esperado, deletamos o ambiente e criamos outro, sem que nada interfira no lado de fora da nossa <em>“caixa”</em>. Faz sentido?</p>
<h3 id="criando-ambientes-virtuais-usando-o-anaconda">Criando Ambientes Virtuais usando o Anaconda</h3>
<p>A sintaxe é simples, algo como:<br>
<code>conda create --name ENV_NAME python=x.x</code></p>
<p>Sendo <em>ENV_NAME</em> justamente o nome do seu ambiente e <em>x.x</em> a versão do Python.</p>
<p><strong>Exemplo:</strong><br>
<code>conda create --name py37 python=3.7</code></p>
<p>Ao fazer o comando acima, será necessário confirmar algumas etapas no Prompt (ou Terminal).</p>
<p>Mas também pode-se fazer direto usando essa sintaxe:<br>
<code>conda create --name py37 python=3.7 -y</code></p>
<p>( <em>-y</em> irá dizer Yes/Sim em todas as etapas e criar o ambiente ).</p>
<h3 id="deletando-um-ambiente-virtual-usando-o-anaconda">Deletando um Ambiente Virtual usando o Anaconda</h3>
<p><code>conda env remove --name ENV_NAME</code></p>
<p>Sendo <em>ENV_NAME</em> o nome usado no ambiente que você deseja deletar.</p>
<p><strong>Exemplo:</strong></p>
<p><code>conda env remove --name py37</code></p>
<h3 id="comandos-úteis-no-anaconda">Comandos úteis no Anaconda:</h3>
<ul>
<li><em>Listando os Ambientes Virtuais</em>:
<blockquote>
<p>conda env list</p>
</blockquote>
</li>
</ul>
<p><em>Na versão conda 4.6+ (funcionando no Windows, Linux e macOS)</em></p>
<ul>
<li>
<p>[ativando um Ambiente Virtual]</p>
<blockquote>
<p><strong>conda activate ENV_NAME</strong></p>
</blockquote>
</li>
<li>
<p>[saindo do Ambiente Virtual]</p>
<blockquote>
<p><strong>conda deactivate</strong></p>
</blockquote>
</li>
</ul>
<p><em>Para versões anteriores ao conda 4.6, usar os seguintes comandos:</em></p>
<blockquote>
<p><em>Windows</em>: <strong>activate ENV_NAME</strong> &amp; <strong>deactivate</strong> (para ativar e desativar Ambientes, respectivamente).</p>
</blockquote>
<blockquote>
<p><em>Linux e macOS</em>: <strong>source activate ENV_NAME</strong> &amp; <strong>source deactivate</strong></p>
</blockquote>
<h3 id="b.-instalando-a-biblioteca-pycryptodome">3.b. Instalando a biblioteca Pycryptodome</h3>
<p><em>[Ative o seu ambiente (suponho que já tenha criado um) e faça o seguinte comando]</em>:</p>
<p><code>pip install pycryptodome</code></p>
<p><em>E se a instalação não sair como o esperado, baixe um pacote Wheel com tudo pronto. [considere a versão do Python que você pretende usar no ambiente, Sistema Operacional e Arquitetura do Computador (32/64bits) ao escolher o download].</em><br>
<a href="https://pypi.org/project/pycryptodome/#files">PYPI | Pycryptodome Downloads</a></p>
<p><em>E instale via pip, fazendo:</em></p>
<p>No Prompt/Terminal, navegue até a pasta em que o arquivo <em>Pycryptodome</em> está e insira o comando <em>pip install</em>, em seguida, copie e cole o nome do arquivo Pycryptodome (não esqueça a extensão .whl):</p>
<p><strong>Exemplo com o Pycryptodome para o Windows, 64 bits e Python 3.7:</strong></p>
<p><code>pip install pycryptodome-3.9.7-cp37-cp37m-win_amd64.whl</code></p>
<h2 id="aes-e-modo-de-operação-cbc">4. AES e modo de operação CBC</h2>
<h3 id="criptografia-aes-mode_cbc">Criptografia AES, MODE_CBC:</h3>
<blockquote>
<p><strong>AES</strong> significa <em>Advanced Encryption Standard</em> — é um padrão de <strong>criptografia</strong> avançada, estabelecida pelo Instituto Nacional de Padrões e Tecnologia (NIST) dos EUA em 2001.</p>
</blockquote>
<blockquote>
<p><strong>MODE_CBC</strong> refere-se ao <strong>modo de operação</strong> em que a cifra trabalha com blocos de dados de tamanho fixo, podendo receber <em>mensagens</em> de qualquer comprimento.</p>
</blockquote>
<h2 id="criador">5. Criador:</h2>
<h4 id="pro.cod3r-instagram"><a href="https://instagram.com/pro.cod3r">PRO.COD3R</a> <em>(Instagram)</em></h4>
</div>
</body>

</html>
