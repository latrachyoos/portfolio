Public Class Form1
    Dim num1, num2 As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        controllo()
        Dim tot As Integer
        tot = Math.Abs(num1 - num2)
        MessageBox.Show(tot)
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        controllo()
        Dim tot, a As Integer
        If num1 > num2 Then
            num2 = a
            num2 = num1
            num1 = a
        End If
        For i = num1 To num2
            tot += i
        Next
        MessageBox.Show(tot)
    End Sub

    Sub controllo()
        If Trim(TextBox1.Text) <> "" And IsNumeric(TextBox1.Text) And Trim(TextBox2.Text) <> "" And IsNumeric(TextBox2.Text) Then
            num1 = TextBox1.Text
            num2 = TextBox2.Text
        End If
    End Sub
End Class
'4. Creare un programma contenente due funzioni
'a. La prima deve restituire la differenza in valore assoluto di due valori passati come parametri. 
'b. La seconda deve restituire la somma dei valori compresi tra i due valori passati come parametri
'Realizzare (ovviamente) anche il codice che richiama le due funzioni prendendo i valori da due caselle di 
'testo. Controllare che i valori inseriti dall’utente siano numerici.