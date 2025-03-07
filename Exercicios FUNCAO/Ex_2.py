def par_ou_impar(num):
    match num % 2 == 0:
        case True:
            return 'Par'
        case False:
            return 'Ímpar'

print(par_ou_impar(5))