Public Class Form1
    Dim parola As String
    Dim ind As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    End Sub

    Sub contr()
        ind += 1
        If Trim(TextBox1.Text) <> "" And IsNumeric(TextBox1.Text) = False And ind = 1 Then
            parola = TextBox1.Text
        End If
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        contr()
        Dim lett, par As String
        lett = LCase(Mid(parola, 1, 1))
        For i = 1 To Len(parola)
            If LCase(Mid(parola, i, 1)) = lett Then
                par &= "*"
            Else
                par &= Mid(parola, i, 1)
            End If
        Next
        TextBox1.Text = par
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        contr()
        Dim par As String
        For i = 1 To Len(parola)
            If i Mod 2 = 0 Then
                par &= "?"
            Else
                par &= Mid(parola, i, 1)
            End If
        Next
        TextBox1.Text = par
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        contr()
        Dim par As String
        Dim cas As Integer
        cas = Int(Rnd() * Len(parola)) + 1
        For i = 1 To Len(parola)
            If i = cas Then
                par &= "!"
            Else
                par &= Mid(parola, i, 1)
            End If
        Next
        TextBox1.Text = par
    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        contr()
        Dim par As String
        Dim cas As Integer
        cas = Int(Rnd() * Len(parola)) + 1
        For i = 1 To Len(parola)
            If i = cas Then
            Else
                par &= Mid(parola, i, 1)
            End If
        Next
        TextBox1.Text = par
    End Sub
End Class
'3. Creare il codice che a partire da una parola inserita dall'utente genera una nuova parola in cui
'A. vengono sostituiti con un asterisco tutti i caratteri uguali al primo carattere della parola (primo 
'carattere compreso)
'B. vengono sostituti con un punto interrogativo tutti i caratteri che si trovano in posizione pari 
'C. viene sostituito con un punto esclamativo un carattere che si trova in una posizione generata a caso.
'D. Eliminare un carattere che si trova in una posizione generata a caso