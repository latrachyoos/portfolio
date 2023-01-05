Public Class Form1
    Dim num As Single
    Dim imp As Single
    Dim a As Single
    Dim b As Single
    Dim c As Single
    Dim d As Single
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        num = TextBox1.Text
        imp += 1
        If imp > 1 Then
            If b <> 0 Then
                a = b
                a += num
            ElseIf c <> 0 Then
                a = c
                a += num
            ElseIf d <> 0 Then
                a = d
                a += num
            Else
                a += num
            End If
        Else
            a += num
        End If
        b = 0
        c = 0
        d = 0
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        num = TextBox1.Text
        imp += 1
        If imp > 1 Then
            If a <> 0 Then
                b = a
                b -= num
            ElseIf c <> 0 Then
                b = c
                b -= num
            ElseIf d <> 0 Then
                b = d
                b -= num
            Else
                b -= num
            End If
        Else
            b += num
        End If
        a = 0
        c = 0
        d = 0
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        num = TextBox1.Text

        imp += 1
        If imp > 1 Then
            If a <> 0 Then
                c = a
                c *= num
            ElseIf b <> 0 Then
                c = b
                c *= num
            ElseIf d <> 0 Then
                c = d
                c *= num
            Else
                c *= num
            End If
        Else
            c += num
        End If
        a = 0
        b = 0
        d = 0
    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        num = TextBox1.Text
        imp += 1
        If imp > 1 Then
            If a <> 0 Then
                d = a
                d /= num
            ElseIf b <> 0 Then
                d = b
                d /= num
            ElseIf c <> 0 Then
                d = c
                d /= num
            Else
                d /= num
            End If
        Else
            d += num
        End If
        a = 0
        b = 0
        c = 0
    End Sub

    Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
        num = TextBox1.Text
        If a <> 0 Then
            a += num
            TextBox1.Text = a
        ElseIf b <> 0 Then
            b -= num
            TextBox1.Text = b
        ElseIf c <> 0 Then
            c *= num
            TextBox1.Text = c
        ElseIf d <> 0 Then
            d /= num
            TextBox1.Text = d
        End If


    End Sub

    Private Sub Button6_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button6.Click
        a = 0
        b = 0
        c = 0
        d = 0
    End Sub
End Class
