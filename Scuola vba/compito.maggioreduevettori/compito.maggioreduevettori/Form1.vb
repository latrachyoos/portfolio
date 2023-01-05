Public Class Form1
    Dim N As Integer = 20
    Dim x(N - 1) As Integer
    Dim y(N - 1) As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        carica()
    End Sub

    Sub carica()
        Randomize()
        For i = 0 To N - 1
            x(i) = Int(Rnd() * 21)
            y(i) = Int(Rnd() * 21)
        Next
    End Sub

    Sub cerca()
        Dim max1, max2 As Integer
        For i = 1 To N - 1
            If x(i) > x(max1) Then
                max1 = i
            End If
            If y(i) > y(max2) Then
                max2 = i
            End If
        Next
        If x(max1) > y(max2) Then
            MessageBox.Show("il piu grande si trova nel primo vettore")
        ElseIf x(max1) = y(max2) Then
            If max1 < max2 Then
                MessageBox.Show("hanno lo stesso numero maggiore ma il primo vettore lo ha prima")
            Else
                MessageBox.Show("hanno lo stesso numero maggiore ma il secondo vettore lo ha prima")
            End If
        Else
            MessageBox.Show("il piu grande si trova nel secondo vettore")
        End If
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        cerca()
    End Sub
End Class
