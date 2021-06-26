import requests

def main():
    print("######################")
    print("#==> CONSULTA CEP <==#")
    print("######################")

    cep_input = ''

    while len(cep_input) != 8:
        cep_input = input("Digite o Cep para consulta:")
        if len(cep_input) != 8:
            print("Quantidade de digitos errada")
        else:
            request = requests.get(
                "https://viacep.com.br/ws/{}/json/".format(cep_input))

    adress = request.json()

    if 'erro' not in adress:
        print("\n########################")
        print("#==> CEP ENCONTRADO <==#")
        print("CEP => {}".format(adress['cep']))
        print('Localidade => {}'.format(adress['localidade']))
        print("Logradouro => {}".format(adress['logradouro']))
        print("Complemento => {}".format(adress['complemento']))
        print('Bairro => {}'.format(adress['bairro']))        
        print('UF = > {}'.format(adress['uf']))
        print('DDD => {}'.format(adress['ddd']))
        print("########################\n")
    else:
        print('\n{} => CEP INVALIDO!\n'.format(cep_input))

    option = int(input("Gostaria de realizar outra consulta? 1(Sim) ou 2(Não)? :"))
    if option == 1:
        main()
    else:
        print("Saindo!!!")

if __name__ == '__main__':
    main()