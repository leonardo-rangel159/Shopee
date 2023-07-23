function Chamada(){
    criar_janela1();
    criar_janela2();
}

function formatar_moeda(valor) {
    return valor.toFixed(2);
}

function formatar_preco(entry, op) {
    try {
        var valor_atual = entry.value;

        // Remover todos os caracteres que não são dígitos numéricos
        valor_atual = valor_atual.replace(/\D/g, '');

        // Adicionar zeros à esquerda na parte decimal
        var parte_decimal = valor_atual.slice(-2);
        var parte_inteira = valor_atual.slice(0, -2);
        parte_inteira = parte_inteira === '' ? '0' : parte_inteira;

        // Inserir a vírgula decimal
        var valor_com_virgula = parte_inteira + '.' + parte_decimal;

        // Converter o valor para número
        var valor_numerico = parseFloat(valor_com_virgula);

        // Formatar o valor monetário com duas casas decimais
        var preco_formatado = formatar_moeda(valor_numerico);
        
        // Atualizar o valor no campo de input
        entry.value = preco_formatado;
        
        calcular(op);

    } catch (error) {
        console.error(error);
    }
}

function calcular(op) {
    try {
        if(op == 1){
            var preco = parseFloat(document.getElementById('preco1').value.replace(/,/g, ''));
            var lucro = parseFloat(document.getElementById('lucro1').value.replace(/,/g, ''));
            var taxa2_checkbox = document.getElementById('taxa2_checkbox1');
            var resultado_label = document.getElementById('resultado1');

            var taxa1 = taxa2_checkbox.checked ? (preco+lucro) * 0.20 : (preco+lucro) * 0.14;
            taxa1 = taxa1 >= 100 ? 100 : taxa1;

            var taxa2 = preco * 0.02;
            var preco_total = preco + lucro + taxa1 + taxa2;

            resultado_label.innerHTML = "Se comprou o produto por " + formatar_moeda(preco) + "<br>"
            + "Então terá que vender por " + formatar_moeda(preco_total) +"<br><br>"
            + "Preço: " + formatar_moeda(preco) + "<br>"
            + "Lucro: " + formatar_moeda(lucro) + "<br>"
            + "Taxa de venda e frete grátis: " + formatar_moeda(taxa1) + "<br>"
            + "Taxa de serviço de transações: " + formatar_moeda(taxa2);
        }
        else{
            var preco = parseFloat(document.getElementById('preco2').value.replace(/,/g, ''));
            var taxa2_checkbox = document.getElementById('taxa2_checkbox2');
            var resultado_label = document.getElementById('resultado2');

            var taxa1 = taxa2_checkbox.checked ? preco * 0.20 : preco * 0.14;
            taxa1 = taxa1 >= 100 ? 100 : taxa1;
            var taxa2 = preco * 0.02;
            var valor = preco - (taxa1 + taxa2);

            resultado_label.innerHTML = "Se o produto está sendo vendido por " + formatar_moeda(preco) + "<br>"
            + "Então o valor do produto com o lucro é " + formatar_moeda(valor) + "<br><br>"
            + "Valor do Produto: " + formatar_moeda(preco) + "<br>"
            + "Taxa de venda e frete grátis: " + formatar_moeda(taxa1) + "<br>"
            + "Taxa de serviço de transações: " + formatar_moeda(taxa2);
        }
    } catch (error) {
        console.error(error);
    }
}

function criar_janela1() {
    var content = `
        <h2>Calcular por quanto vender</h2>

        <div class="checkbox-container">
            <input type="checkbox" id="taxa2_checkbox1" onclick="calcular(1)">
            <label for="taxa2_checkbox1">Adicionar Taxa2</label>
        </div>

        <div class="input-container">
            <label for="preco1">Qual valor você pagará pelo produto:</label>
            <input type="txt" id="preco1" value="0.00" onkeyup="formatar_preco(this,1)">
        </div>

        <div class="input-container">
            <label for="lucro1">Quanto deseja ganhar de lucro em cima do produto:</label>
            <input type="txt" id="lucro1" value="0.00" onkeyup="formatar_preco(this,1)">
        </div>
        
        <br>
        <div class="result-container" id="resultado1"></div>
    `;

    document.getElementById("venda").innerHTML = content;
}

function criar_janela2() {
    var content = `
        <h2>Calcular por quanto estão vendendo</h2>

        <div class="checkbox-container">
            <input type="checkbox" id="taxa2_checkbox2" onclick="calcular(2)">
            <label for="taxa2_checkbox2">Frete grátis</label>
        </div>

        <div class="input-container">
            <label for="preco2">Qual valor do produto:</label>
            <input type="text" value="0.00" id="preco2" onkeyup="formatar_preco(this,2)">
        </div>

        <br>

        <div class="result-container" id="resultado2"></div>
    `;

    document.getElementById("produto").innerHTML = content;
}