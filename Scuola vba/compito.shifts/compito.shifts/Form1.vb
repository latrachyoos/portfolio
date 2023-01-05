Public Class Form1
    Const Nmax As Byte = 50
    Dim x(Nmax) As Integer
    Dim N As Integer = 10
    Dim file As String = "numeri.txt"
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        'riempi()
        'salva()
        carica()
        visua()
    End Sub

    Sub riempi()
        Randomize()
        For i = 0 To N - 1
            x(i) = Int(Rnd() * 20) + 1
        Next
    End Sub

    Sub visua()
        ListBox1.Items.Clear()
        For i = 0 To N - 1
            ListBox1.Items.Add(x(i))
        Next
    End Sub

    Sub carica()
        Dim k As Byte
        FileOpen(1, file, OpenMode.Input)
        Do While Not EOF(1)
            x(k) = LineInput(1)
            k += 1
        Loop
        FileClose(1)
    End Sub

    Sub salva()
        FileOpen(1, file, OpenMode.Output)
        For i = 0 To N - 1
            PrintLine(1, x(i))
        Next
        FileClose(1)
    End Sub

    Sub elimina(ByVal ind As Byte)
        For i = ind To N - 2
            x(i) = x(i + 1)
        Next
        x(N - 1) = 0
        N -= 1
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim ind As Integer
        ind = ListBox1.SelectedIndex
        If ind >= 0 Then
        Else
            ind = Int(Rnd() * N)
        End If
        elimina(ind)
        visua()
    End Sub

    Sub aggiungi(ByVal ind As Byte)
        For i = N - 1 To ind Step -1
            x(i + 1) = x(i)
        Next
        x(ind) = Int(Rnd() * 20) + 1
        N += 1
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim ind As Integer
        ind = ListBox1.SelectedIndex
        If ind >= 0 Then
        Else
            ind = Int(Rnd() * N)
        End If
        aggiungi(ind)
        visua()
    End Sub
End Class
