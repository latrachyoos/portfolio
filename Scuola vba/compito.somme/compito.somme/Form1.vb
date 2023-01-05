Public Class Form1
    Const N As Integer = 3
    Dim x(N - 1, N - 1) As Integer

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        riempi()
        formatta()
    End Sub

    Sub riempi()
        Randomize()
        For r = 0 To N - 1
            For c = 0 To N - 1
                x(r, c) = Int(Rnd() * N * N) + 1
            Next
        Next
    End Sub

    Sub formatta()
        dgvdati.Columns.Clear()
        dgvdati.Rows.Clear()
        For c = 0 To N - 1
            dgvdati.Columns.Add("col", c)
            dgvdati.Columns(c).Width = 40
        Next
        visua()
    End Sub

    Sub visua()
        For r = 0 To N - 1
            dgvdati.Rows.Add()
            For c = 0 To N - 1
                dgvdati.Rows(r).Cells(c).Value = x(r, c)
            Next
        Next
    End Sub
    
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        MessageBox.Show("sotto prima diagonle " & somma1() & vbCrLf & "sopra seconda diagonle " & somma2() & vbCrLf & "sopra prima diagonle " & somma3() & vbCrLf & "sotto seconda diagonle " & somma4())
    End Sub

    Function somma1() As Integer
        Dim som As Integer
        For r = 0 To N - 1
            For c = 0 To r
                som += x(r, c)
            Next
        Next
        Return som
    End Function

    Function somma2() As Integer
        Dim som As Integer
        For c = 0 To N - 1
            For r = 0 To c
                som += x(r, c)
            Next
        Next
        Return som
    End Function

    Function somma3() As Integer
        Dim som As Integer
        For r = 0 To N - 1
            For c = 0 To N - 1 - r
                som += x(r, c)
            Next
        Next
        Return som
    End Function

    Function somma4() As Integer
        Dim som As Integer
        For r = 0 To N - 1
            For c = N - 1 - r To N - 1
                som += x(r, c)
            Next
        Next
        Return som
    End Function
End Class
