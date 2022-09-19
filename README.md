# data-extraction-client-server
#### Aplicação de consulta de dados cliente-servidor utilizando o módulo socket do python em que os dados trocados entre as duas partes são ambos criptografados usando um algoritmo RSA.
É importante ressaltar que essa criptografia quando é feita para fins profissionais possui valores primos P e Q na ordem de 10^10, mas como este projeto possui fins acadêmicos utilizou-se valores primos bem menores, tornando assim o código mais frágil. Porém podem-se aumentar este valor a depender da relação entre segurança desejada e capacidade de processamento disponível.

Futuras melhorias:
- [x] Aplicar a criptografia tanto no servidor quanto no cliente
- [ ] Corrigir o erro de loop ao receber um ID inválido (ID<0 ou ID>4)
- [ ] Gerar números primos aleatórios e maiores
- [ ] Tornar a variável column mais flexível, testando se seu valor existe nas colunas do dicionário sem adicionar mais Ifs desnecessários ao código
- [ ] Fazer com que os testes de validação das variáveis column e idNumber ocorram separadamente, ou seja ao inserir o valor em uma delas, este valor já é testado no servidor recebendo ou não uma validação.

