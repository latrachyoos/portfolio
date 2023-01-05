Public Class Form1
    Const max As Integer = 15
    Dim x(max) As Integer

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        fai()
    End Sub
    Sub fai()
        Dim n, cont, count As Integer
        Dim i As Integer = 0
        Dim si As Integer = -1
        Randomize()
        x(0) = Rnd() * 14 + 1
        ListBox1.Items.Add(x(0))
        Do While i < max - 1
            Randomize()
            si = -1
            cont += 1
            n = Rnd() * 14 + 1
            For k = 0 To i
                If n <> x(k) Then
                    si += 1
                    count += 1
                End If
            Next
            'i += 1
            If si = i Then
                i += 1
                x(i) = n
                ListBox1.Items.Add(n)
            End If
        Loop
        MessageBox.Show("while " & cont & vbCrLf & "for " & count)
    End Sub
    Private Sub click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Click
        ListBox1.Items.Clear()
        Dim s(max) As Integer
        Dim n As Integer
        For i = 0 To 14
            Select Case x(i)
                Case 1
                    n = x(i)
                    s(n - 1) = n
                Case 2
                    n = x(i)
                    s(n - 1) = n
                Case 3
                    n = x(i)
                    s(n - 1) = n
                Case 4
                    n = x(i)
                    s(n - 1) = n
                Case 5
                    n = x(i)
                    s(n - 1) = n
                Case 6
                    n = x(i)
                Case 7
                    n = x(i)
                Case 8
                    n = x(i)
                    s(n - 1) = n
                Case 9
                    n = x(i)
                    s(n - 1) = n
                Case 10
                    n = x(i)
                    s(n - 1) = n
                Case 11
                    n = x(i)
                    s(n - 1) = n
                Case 12
                    n = x(i)
                    s(n - 1) = n
                Case 13
                    n = x(i)
                    s(n - 1) = n
                Case 14
                    n = x(i)
                    s(n - 1) = n
                Case 15
                    n = x(i)
                    s(n - 1) = n
            End Select
        Next
        For i = 0 To 14
            ListBox1.Items.Add(s(i))
        Next
    End Sub
End Class
'15 ele, 1 e 15