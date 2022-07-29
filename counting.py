#I hve one stock that pays a constant value every month
#I buy one every month
#I keep the value I received from the previous ones + the money I receive from the new one 

stockPays = 0.87 #valor pago mensalmente pela ação
n = int(input("Numero de ações: ")) #numero de ações que a pessoa tem
stockMonthlyPay = stockPays * n  #calculo de pagamento mensal: valor Mensal * numero de ações que a pessoa tem
stockWallet = stockMonthlyPay #valor em carteira produto do calculo anterior
totalStock = stockWallet + stockMonthlyPay #valor total: pagamento mensal + o que a pessoa já tinha em carteira
print("valor mensal recebido com ", n, "ações", stockMonthlyPay) 
print("valor recebido mensalmente + valor que ja estava em carteira; ", totalStock)
print("Você tem: ", n, "ações")
print("suas ações pagam: ", stockPays, "ao mês")