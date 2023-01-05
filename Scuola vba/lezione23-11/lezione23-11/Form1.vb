Imports System.Data.OleDb 'come se fosse una libreria

Public Class Form1

    Dim strcon As String = "provider=microsoft.ace.oledb.12.0; data source = nw.mdb" 'provider microsoft: ace.oledb.12.0, jet.oledb.4.0
    'Dim connessione As New OleDbConnection 'dichiaro ed istanzio
    'non si possono utilizzare funzioni come global
    Dim FILE As String = "file.csv"

    Private Sub btnfaqualcosa_Click(sender As System.Object, e As System.EventArgs) Handles btnfaqualcosa.Click

        Try
            Dim connessione As New OleDbConnection 'dichiarato l'oggetto, dove si potrà utilizzare l'oggetto definisce l'ambito di validità (scope)
            'connessione = New OleDbConnection 'istanziato l'oggetto
            'bisogna indicare con quale dbms bisogna lavorare, chi è il bdms
            Dim comando As New OleDbCommand
            Dim SQL As String
            Dim nomesocieta As String
            connessione.ConnectionString = strcon
            connessione.Open()
            comando.Connection = connessione
            SQL = "select nomesocieta from clienti where idcliente = 'ALFKI'"
            comando.CommandText = SQL 'da un valore a comando che verra mandato dopo
            nomesocieta = comando.ExecuteScalar()
            MsgBox(nomesocieta)
            connessione.Close()
            MsgBox("connessione eseguita")
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub

    Private Sub btnnazioni_Click(sender As System.Object, e As System.EventArgs) Handles btnnazioni.Click
        Try
            Dim connessione As New OleDbConnection 
            Dim comando As New OleDbCommand
            Dim lettore As OleDbDataReader 'unico oggetto che non deve essre istanziato, è una tabella contenete tutti i tipi di dati,=
            'si modella in base ai dati restituiti dalla query, non può essere prestabilito
            'Dim SQL As String
            connessione.ConnectionString = strcon
            connessione.Open()
            comando.Connection = connessione
            'SQL = 
            comando.CommandText = "select distinct nazione from clienti"
            lettore = comando.ExecuteReader 'in combinazione con un data reader
            Do While lettore.Read 'come se fosse booleana, se trova da leggere TRUE se non c'è più niente FALSE, prende un record alla volta
                cmbnazioni.Items.Add(lettore.Item("nazione")) 'seleziono il campo da prendere che è già presente nella query in SELECT, con o senza .item
            Loop
            connessione.Close()
            'MsgBox("connessione eseguita")
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try

    End Sub

    Private Sub btnclienti_Click(sender As System.Object, e As System.EventArgs) Handles btnclienti.Click
        ListBox1.Items.Clear()
        Try
            Dim connessione As New OleDbConnection
            Dim comando As New OleDbCommand
            Dim lettore As OleDbDataReader
            connessione.ConnectionString = strcon
            connessione.Open()
            comando.Connection = connessione
            comando.CommandText = "select nomesocieta from clienti where nazione = '" & cmbnazioni.Text & "'" 'legge la nazione scelta da combo, prima carica combo
            lettore = comando.ExecuteReader
            Do While lettore.Read
                ListBox1.Items.Add(lettore("nomesocieta"))
            Loop
            connessione.Close()
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try

    End Sub



    Private Sub sendquery_Click(sender As System.Object, e As System.EventArgs) Handles sendquery.Click

       Try
            Dim connessione As New OleDbConnection
            Dim comando As New OleDbCommand
            Dim lettore As OleDbDataReader
            'Dim riga As Integer
            Dim str As String
            connessione.ConnectionString = strcon
            connessione.Open()
            comando.Connection = connessione
            comando.CommandText = txtquery.Text 'legge la nazione scelta da combo, prima carica combo
            lettore = comando.ExecuteReader
            'MsgBox(lettore.FieldCount) 'fieldcount mi da numero colonne
            'dgv.Rows.Clear()
            'dgv.Columns.Clear()
           
            If lettore.HasRows Then
                FileOpen(1, FILE, OpenMode.Output)
                lettore.Close()
                lettore = comando.ExecuteReader
                Do While lettore.Read
                    str = ""
                    For k = 0 To lettore.FieldCount - 1
                        str &= lettore(k) & ";"
                    Next
                    PrintLine(1, Mid(str, 1, Len(str) - 1))
                Loop
                FileClose()
            Else
                MsgBox("QUERY SENZA SOLUZIONI")
            End If

            connessione.Close()
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try

    End Sub

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click


    End Sub
End Class
