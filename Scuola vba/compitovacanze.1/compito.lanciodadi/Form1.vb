Public Class Form1

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim dadi, num, max, min As Integer
        If Trim(TextBox2.Text) = "" Then
            max = 6
        Else
            max = TextBox1.Text
        End If
        If Trim(TextBox1.Text) = "" Then
            dadi = 2
        Else
            dadi = TextBox1.Text
        End If
        For i = 0 To dadi - 1
            num += Int(Rnd() * max) + 1
        Next
        ListBox1.Items.Add(num)
    End Sub

End Class
