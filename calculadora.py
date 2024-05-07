def soma(a, b)
    return a + b

if __name__ == "__main__":
  num1 = float(intup("Digite o primeiro número: "))
  num2 = float(intup("Digite o segundo número: "))
  resultado = soma(num1, num2)
  print("resultado: {resultado}".format(resultado))
