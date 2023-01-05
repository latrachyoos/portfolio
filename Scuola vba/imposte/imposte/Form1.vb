Public Class Form1
    Dim importo As Single
    Dim imposte As Single
    Dim sc1 As Single
    Dim sc2 As Single
    Dim aliq1 As Single
    Dim aliq2 As Single
    Dim aliq3 As Single
    Dim parziale As Single
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        importo = TextBox1.Text
        sc1 = 10000
        sc2 = 20000
        aliq1 = 0.1
        aliq2 = 0.12
        aliq3 = 0.15
        parziale = sc1 * aliq1
        If importo > 10000 Then
            If importo > 20000 Then
                imposte = (importo - sc2) * aliq3 + sc1 * aliq2
            Else
                imposte = (importo - sc1) * aliq2

            End If
            imposte += parziale
        Else
            imposte = importo * aliq1
        End If
        TextBox2.Text = imposte
    End Sub

End Class
