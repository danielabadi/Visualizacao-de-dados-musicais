import imports_datasets as imports

x = imports.df_mix2.groupby(['month', 'day']).size()
x = x.reset_index(level=0)
x = x.reset_index(level=0)
x.rename( columns={0 :'quantidade'}, inplace=True )

lista = []
for i in range(1, 13):
  dias = x[x['month'] == i]
  mes = []
  for dia in range(1, 32):
    if len(dias[dias['day'] == dia]) == 0:
      mes.append(0)
    else:
      mes.append(dias[dias['day'] == dia]['quantidade'].iloc[0])
  lista.append(mes)

  lista[0][0] = 0
fig = imports.px.imshow(lista,x=list(range(1, 32)), y=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 
                                               'Agosto','Setembro', 'Outubro', 'Novembro','Dezembro'], 
                labels=dict(color='Número de<br>músicas'), )