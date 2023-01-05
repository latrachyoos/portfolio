Public Class Form1

    Const max As Integer = 15
    Dim x(max) As Integer

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        fai()
    End Sub
    Sub fai()
        Dim n, cont, count As Integer
        Dim i, k As Integer
        Dim si As Boolean = False
        Randomize()
        x(0) = Rnd() * 14 + 1
        ListBox1.Items.Add(x(0))
        Do While i < max - 1
            Randomize()
            cont += 1
            n = Rnd() * 14 + 1
            'MessageBox.Show(k & vbCrLf & i)
            k = 0
            si = False
            Do While k <= i And si = False
                count += 1
                If n = x(k) Then
                    si = True
                End If
                k += 1
            Loop
            'MessageBox.Show(si)
            If si = False Then
                i += 1
                x(i) = n
                ListBox1.Items.Add(n)
            End If
        Loop
        MessageBox.Show("while " & cont & vbCrLf & "for " & count)
    End Sub
End Class