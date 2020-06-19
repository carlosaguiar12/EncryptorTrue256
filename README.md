<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>teste</title>
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
<p>Exemplos de Encriptação/Decriptação</p>
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
<h2 id="exemplos-de-encriptaçãodecriptação">4. Exemplos de Encriptação/Decriptação</h2>
<h3 id="criptografia-aes-mode_cbc">Criptografia AES, MODE_CBC:</h3>
<blockquote>
<p><strong>AES</strong> significa <em>Advanced Encryption Standard</em> — é um padrão de <strong>criptografia</strong> avançada, estabelecida pelo Instituto Nacional de Padrões e Tecnologia (NIST) dos EUA em 2001.</p>
</blockquote>
<blockquote>
<p><strong>MODE_CBC</strong> refere-se ao <strong>modo de operação</strong> em que a cifra trabalha com blocos de dados de tamanho fixo, podendo receber <em>mensagens</em> de qualquer comprimento.</p>
</blockquote>
<h3 id="criptografando----exemplo-i">Criptografando  /  Exemplo I:</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment">#importações</span>
<span class="token keyword">import</span> os
<span class="token keyword">from</span> Crypto<span class="token punctuation">.</span>Cipher <span class="token keyword">import</span> AES
<span class="token keyword">from</span> Crypto<span class="token punctuation">.</span>Util<span class="token punctuation">.</span>Padding <span class="token keyword">import</span> pad

<span class="token comment">#Chave de exemplo (JAMAIS compartilhe ou perca a sua Chave Real)</span>
key <span class="token operator">=</span> b<span class="token string">'f\x9c\xea\x8f\xce\x1b\x89\xe3\xc8\xad,\n8\xa0M\xbbsj\xe2\x8e\xe7\\\xeb\xa3\xbfMo\x16\xcd\xcc\xbf_'</span>

<span class="token comment">#insira o caminho de um arquivo para teste</span>
file_name <span class="token operator">=</span> <span class="token string">'insira_aqui_um_arquivo.txt'</span>

<span class="token comment">#lendo o arquivo como sequência binária</span>
<span class="token keyword">with</span> <span class="token builtin">open</span><span class="token punctuation">(</span>file_name<span class="token punctuation">,</span> <span class="token string">'rb'</span><span class="token punctuation">)</span> <span class="token keyword">as</span> file_object<span class="token punctuation">:</span>
    plaintext <span class="token operator">=</span> file_object<span class="token punctuation">.</span>read<span class="token punctuation">(</span><span class="token punctuation">)</span>  <span class="token comment"># conteúdo do arquivo</span>

<span class="token comment">#criando um objeto cifra com a chave no MODE_CBC</span>
cipher <span class="token operator">=</span> AES<span class="token punctuation">.</span>new<span class="token punctuation">(</span>key<span class="token punctuation">,</span> AES<span class="token punctuation">.</span>MODE_CBC<span class="token punctuation">)</span>  <span class="token comment"># inicialização da criptografia</span>

<span class="token comment">#==== criptografando os dados ====#</span>
data_ciphered <span class="token operator">=</span> cipher<span class="token punctuation">.</span>encrypt<span class="token punctuation">(</span>pad<span class="token punctuation">(</span>plaintext<span class="token punctuation">,</span> AES<span class="token punctuation">.</span>block_size<span class="token punctuation">)</span><span class="token punctuation">)</span>
  
<span class="token comment">#adicionando a extensão '.enc' no arquivo</span>
<span class="token keyword">with</span> <span class="token builtin">open</span><span class="token punctuation">(</span>file_name <span class="token operator">+</span> <span class="token string">'.enc'</span><span class="token punctuation">,</span> <span class="token string">'wb'</span><span class="token punctuation">)</span> <span class="token keyword">as</span> file_object<span class="token punctuation">:</span>
    <span class="token comment">#escrevendo o vetor de inicialização e os dados encriptados no arquivo</span>
    file_object<span class="token punctuation">.</span>write<span class="token punctuation">(</span>cipher<span class="token punctuation">.</span>iv<span class="token punctuation">)</span>
    file_object<span class="token punctuation">.</span>write<span class="token punctuation">(</span>data_ciphered<span class="token punctuation">)</span>

<span class="token comment">#deletando o arquivo original</span>
os<span class="token punctuation">.</span>remove<span class="token punctuation">(</span>file_name<span class="token punctuation">)</span>
</code></pre>
<blockquote>
<p>Dica: você colocar os códigos de exemplo dentro de uma função e receber vários arquivos por meio de iterações/<em>loops</em>. [ Veja o código completo no repositório para mais detalhes | arquivo: encryptor_pro_cod3r.py ].</p>
</blockquote>
<h3 id="descriptografando--exemplo-ii">Descriptografando / Exemplo II:</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment">#importações</span>
<span class="token keyword">import</span> os
<span class="token keyword">from</span> Crypto<span class="token punctuation">.</span>Cipher <span class="token keyword">import</span> AES
<span class="token keyword">from</span> Crypto<span class="token punctuation">.</span>Util<span class="token punctuation">.</span>Padding <span class="token keyword">import</span> unpad

<span class="token comment">#Chave de exemplo (JAMAIS compartilhe ou perca a sua Chave Real)</span>
key <span class="token operator">=</span> b<span class="token string">'f\x9c\xea\x8f\xce\x1b\x89\xe3\xc8\xad,\n8\xa0M\xbbsj\xe2\x8e\xe7\\\xeb\xa3\xbfMo\x16\xcd\xcc\xbf_'</span>

<span class="token comment">#Insira um arquivo encriptado</span>
file_name <span class="token operator">=</span> <span class="token string">'insira_um_arquivo_aqui.enc'</span>

<span class="token comment">#lendo o arquivo como sequência binária</span>
<span class="token keyword">with</span> <span class="token builtin">open</span><span class="token punctuation">(</span>file_name<span class="token punctuation">,</span> <span class="token string">'rb'</span><span class="token punctuation">)</span> <span class="token keyword">as</span> file_object<span class="token punctuation">:</span>
    <span class="token comment">#vetor de inicialização com os 16 bytes necessários</span>
    iv <span class="token operator">=</span> file_object<span class="token punctuation">.</span>read<span class="token punctuation">(</span><span class="token number">16</span><span class="token punctuation">)</span>
    <span class="token comment">#leitura do resto dos dados</span>
    data_ciphered <span class="token operator">=</span> file_object<span class="token punctuation">.</span>read<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token comment">#criando um objeto cifra com a chave no MODE_CBC</span>
cipher <span class="token operator">=</span> AES<span class="token punctuation">.</span>new<span class="token punctuation">(</span>key<span class="token punctuation">,</span> AES<span class="token punctuation">.</span>MODE_CBC<span class="token punctuation">,</span> iv<span class="token operator">=</span>iv<span class="token punctuation">)</span>  <span class="token comment"># inicialização da criptografia</span>

<span class="token comment">#dados restaurados prontos para a saída</span>
data_restore <span class="token operator">=</span> unpad<span class="token punctuation">(</span>cipher<span class="token punctuation">.</span>decrypt<span class="token punctuation">(</span>data_ciphered<span class="token punctuation">)</span><span class="token punctuation">,</span> AES<span class="token punctuation">.</span>block_size<span class="token punctuation">)</span>

<span class="token comment">#reescrevendo o arquivo sem a extensão '.enc'</span>
<span class="token keyword">with</span> <span class="token builtin">open</span><span class="token punctuation">(</span>file_name<span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token operator">-</span><span class="token number">4</span><span class="token punctuation">]</span><span class="token punctuation">,</span> <span class="token string">'wb'</span><span class="token punctuation">)</span> <span class="token keyword">as</span> file_object<span class="token punctuation">:</span>
    file_object<span class="token punctuation">.</span>write<span class="token punctuation">(</span>data_restore<span class="token punctuation">)</span>

<span class="token comment">#deletando o arquivo original</span>
os<span class="token punctuation">.</span>remove<span class="token punctuation">(</span>file_name<span class="token punctuation">)</span>
</code></pre>
<h2 id="criador">5. Criador:</h2>
<h4 id="pro.cod3r-instagram"><a href="https://instagram.com/pro.cod3r">PRO.COD3R</a> <em>(Instagram)</em></h4>
</div>
</body>

</html>
