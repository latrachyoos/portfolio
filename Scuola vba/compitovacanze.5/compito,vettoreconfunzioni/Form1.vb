Public Class Form1
    Const N As Integer = 100
    Dim I As Integer
    Dim p(N - 1) As String
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim str As String
        FileOpen(1, "parole.txt", OpenMode.Input)
        Do While Not EOF(1)
            I += 1
            str = LineInput(1)
            p(I - 1) = str
        Loop
        FileClose(1)
        carica()
    End Sub

    Sub carica()
        ListBox1.Items.Clear()
        For t = 0 To I - 1
            ListBox1.Items.Add(p(t))
        Next
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        If Trim(TextBox1.Text) <> "" And IsNumeric(TextBox1.Text) = False Then
            decisione()
            I += 1
            p(I - 1) = TextBox1.Text
        End If
        TextBox1.Clear()
        carica()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        If I > 0 Then
            For t = 0 To I - 2
                p(t) = p(t + 1)
            Next
            I -= 1
        End If
        carica()
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        Dim ind As Integer
        ind = ListBox1.SelectedIndex
        If ind <> -1 Then
            cancella(ind)
            I -= 1
        End If
        carica()
    End Sub

    Sub cancella(ByVal ind As Integer)
        For t = ind To I - 2
            p(t) = p(t + 1)
        Next
    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        Dim l(N / 2 - 1) As String
        Dim lett As String
        Dim num As Integer
        If Trim(Len(TextBox1.Text)) = 1 Then
            lett = TextBox1.Text
            For t = 0 To I - 1
                If LCase(lett) = LCase(Mid(p(t), 1, 1)) Then
                    l(num) = p(t)
                    num += 1
                End If
            Next
        End If
        TextBox1.Clear()
        ListBox2.Items.Clear()
        For t = 0 To num - 1
            ListBox2.Items.Add(l(t))
        Next
        MessageBox.Show(num)
    End Sub

    Sub decisione()
        Dim alt As Boolean = True
        If RadioButton1.Checked Then
        ElseIf RadioButton2.Checked Then
            alt = False
        End If
        If alt Then
            TextBox1.Text = UCase(TextBox1.Text)
        Else
            TextBox1.Text = LCase(TextBox1.Text)
        End If
    End Sub

    Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
        FileOpen(1, "parole.txt", OpenMode.Output)
        For t = 0 To I - 1
            PrintLine(1, p(t))
        Next
        FileClose(1)
    End Sub
End Class
'5. Creare un programma che permetta le seguenti operazioni:
'A. Inserire dei valori testuali in un vettore
'B. Visualizzare il vettore in una listbox
'C. Cancellare il primo elemento del vettore
'D. Cancellare il valore presente in un elemento del vettore selezionandolo da una lista (il codice di 
'visualizzazione dei dati nella lista deve essere realizzato mediante procedura)
'E. Caricare in una lista i valori che iniziano con una lettera immessa da un utente in una TextBox
'F. Contare il numero di parole che iniziano con la stessa lettera di una parola immessa da un utente
'in una TextBox
'G. Sulla base della scelta fatta dall'utente mediante due pulsanti di opzione (radiobutton) convertire 
'in maiuscolo o in minuscolo tutti i valori inseriti nel vettore (uso delle funzioni Ucase e Lcase). A 
'seguire visualizzare il vettore nella lista
'H. Salvare i valori presenti nel vettore in un file sequenziale e ricaricarli all'apertura del programma