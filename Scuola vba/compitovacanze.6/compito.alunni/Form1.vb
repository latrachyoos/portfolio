Public Class Form1
    Const I As Integer = 50
    Dim ind As Integer
    Dim n(I - 1), c(I - 1) As String
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim str As String
        FileOpen(1, "nomi.txt", OpenMode.Input)
        Do While Not EOF(1)
            str = LineInput(1)
            ind += 1
            n(ind - 1) = str
        Loop
        FileClose(1)
        ind = 0
        FileOpen(2, "cognome.txt", OpenMode.Input)
        Do While Not EOF(2)
            str = LineInput(2)
            ind += 1
            c(ind - 1) = str
        Loop
        FileClose(2)
        carica()
    End Sub

    Sub carica()
        ListBox1.Items.Clear()
        For t = 0 To ind - 1
            ListBox1.Items.Add(n(t) & " " & c(t))
        Next
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim nome, cognome As String
        If Trim(TextBox1.Text) <> "" And Trim(TextBox2.Text) <> "" Then
            ind += 1
            nome = Trim(TextBox1.Text)
            cognome = Trim(TextBox2.Text)
            n(ind - 1) = nome
            c(ind - 1) = cognome
            carica()
        End If
        
    End Sub

    Sub cambio(ByVal t As Integer, ByVal v As Integer)
        Dim a, b As String
        a = c(t)
        b = n(t)
        c(t) = c(v)
        c(v) = a
        n(t) = n(v)
        n(v) = b
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim v As Integer = 0
        If ind > 1 Then
            For t = 0 To ind - 2
                For v = t + 1 To ind - 1
                    If c(v) < c(t) Then
                        cambio(t, v)
                    End If
                Next
            Next
        End If
        carica()
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        Dim v As Integer = 0
        If ind > 1 Then
            For t = 0 To ind - 2
                For v = t + 1 To ind - 1
                    If c(v) < c(t) Then
                        cambio(t, v)
                    ElseIf c(v) = c(t) Then
                        If n(v) < n(t) Then
                            cambio(t, v)
                        End If
                    End If
                Next

            Next
        End If
        carica()
    End Sub

    Sub elimina(ByVal sel As Integer)
        For t = sel To ind - 2
            c(t) = c(t + 1)
            n(t) = n(t + 1)
        Next
        n(ind - 1) = ""
        c(ind - 1) = ""
        ind -= 1
    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        Dim sel As Integer
        sel = ListBox1.SelectedIndex
        If sel <> -1 Then
            elimina(sel)
            carica()
        End If
    End Sub

    Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
        FileOpen(1, "nomi.txt", OpenMode.Output)
        For t = 0 To ind - 1
            PrintLine(1, n(t))
        Next
        FileClose(1)
        FileOpen(2, "cognome.txt", OpenMode.Output)
        For t = 0 To ind - 1
            PrintLine(2, c(t))
        Next
        FileClose(2)
    End Sub
End Class
'6. Creare un programma che dopo aver permesso l’inserimento di cognomi e nomi in due vettori paralleli, 
'permetta di
'a. Visualizzare cognome e nome in un'unica listbox.
'b. Ordinare i vettori sulla base dei cognomi (i dati della lista devono essere aggiornati sulla base 
'dell’ordinamento)
'c. Ordinare i vettori sulla base del cognome e nel caso siano uguali confrontare i nomi (i dati presenti 
'nella listbox devono essere aggiornati dopo aver fatto l'ordinamento)
'd. Cancellare i dati di un alunno selezionato mediante la listbox (i dati vanno cancellati da entrambi i 
'vettori)
'e. Salvare i dati dei due vettori in due files sequenziali.
'f. All'avvio del programma ricaricare nei due vettori i valori presenti nei due file