Public Class Form1

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        
    End Sub

    Dim num, num2 As Integer
    Dim segno As String
    Sub forma()
        num = 0
        If TextBox1.Text = "impossibile" Then
            num = 0
        Else
            If IsNumeric(TextBox1.Text) Then
                num = TextBox1.Text
            End If
        End If
    End Sub

    Sub controllo()
        If IsNumeric(TextBox1.Text) Then
            num2 = TextBox1.Text
        End If
    End Sub

    Sub azzera()
        TextBox1.Clear()
        TextBox1.Focus()
    End Sub

    Sub lista()
        ListBox1.Items.Add(num & segno & num2 & "= " & TextBox1.Text)
    End Sub

    Dim som, dif, pro, div As Integer
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        forma()
        segno = "+"
        azzera()
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        forma()
        segno = "-"
        azzera()
    End Sub

    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        forma()
        segno = "x"
        azzera()
    End Sub

    Private Sub Button4_Click(sender As System.Object, e As System.EventArgs) Handles Button4.Click
        forma()
        segno = ":"
        azzera()
    End Sub

    Private Sub Button5_Click(sender As System.Object, e As System.EventArgs) Handles Button5.Click
        Select Case segno
            Case "+"
                controllo()
                TextBox1.Text = num + num2
            Case "-"
                controllo()
                TextBox1.Text = num - num2
            Case "x"
                controllo()
                TextBox1.Text = num * num2
            Case ":"
                controllo()
                If num2 <> 0 Then
                    TextBox1.Text = num / num2
                Else
                    TextBox1.Text = "impossibile"
                End If
        End Select
        lista()
    End Sub
End Class
