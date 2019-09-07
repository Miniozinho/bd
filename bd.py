#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

con = pymysql.connect(host='127.0.0.1',
                      user='miniozinho',
                      password='senha',
                      db='tarefas',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)

x=1
while (x ==1):
  print("")
  print("Selecione o que voce deseja fazer")
  print("1: Listar tarefas")
  print("2: Cadastrar Tarefa")
  print("3: Concluir tarefa")
  print("4: excluir tarefa")
  print("")
  x= int(input())
  if x ==1:
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM lista")
      rows = cur.fetchall()
      print("")
      for row in rows:
        print(row["idlista"], row["nome"],row["data"],row["prioridade"],row["conclusao"])
  elif x==2:
    print("Qual o nome da tarefa?")
    nome = str(input())
    print("Que dia?")
    dia = str(input())
    print("De que mes?")
    mes = str(input())
    print("De que ano?")
    ano = str(input())
    data = dia + "/" + mes + "/" + ano
    print("qual a prioridade dessa tarefa?(1-2-3)")
    prioridade = str(input())
    with con:
      cur = con.cursor()
      sql = "INSERT INTO `lista` (`nome`, `data`, `prioridade`) VALUES (%s, %s, %s)"
      cur.execute(sql, (nome, data, prioridade))
  elif x==3:
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM lista")
      rows = cur.fetchall()
      print("")
      for row in rows:
        print(row["idlista"], row["nome"],row["data"],row["prioridade"],row["conclusao"])
    print("selecione o id da tarefa que deseja concluir")
    exc = str(input())
    with con:
      sql = "UPDATE lista SET conclusao='[V]' WHERE idlista = %s;"
      cur.execute(sql, (exc))
  elif x==4:
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM lista")
      rows = cur.fetchall()
      print("")
      for row in rows:
        print(row["idlista"], row["nome"],row["data"],row["prioridade"],row["conclusao"])

    print("selecione o id da tarefa que deseja excluir")
    exc = str(input())
    with con:
      sql = "DELETE FROM lista WHERE idlista = %s;"
      cur.execute(sql, (exc))

