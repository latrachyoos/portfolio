Public Class Form1
    Dim N As Integer = 7
    Dim M(N - 1, N - 1) As Integer

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        crea()
    End Sub

    Sub crea()
        Randomize()
        For r = 0 To N - 1
            For c = 0 To N - 1
                M(r, c) = Int(Rnd() * N) + 1
            Next
        Next
        visua()
    End Sub

    Sub visua()
        dgvdati.Rows.Clear()
        dgvdati.Columns.Clear()
        dgvdati.ColumnCount = N
        dgvdati.Rows.Add(N - 1)
        For r = 0 To N - 1
            For c = 0 To N - 1
                dgvdati.Rows(r).Cells(c).Value = (M(r, c))
            Next
        Next
    End Sub

    Sub cerca(ByVal num As Integer)
        Dim cont As Integer
        For i = 0 To N - 1
            If M(i, i) = num Then
                cont += 1
            End If
            If i <> N - i - 1 Then
                If M(i, N - i - 1) = num Then
                    cont += 1
                End If
            End If
        Next
        MessageBox.Show(cont)
    End Sub

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim num As Integer
        If IsNumeric(TextBox1.Text) Then
            num = TextBox1.Text
            cerca(num)
        Else
            num = dgvdati.Rows(dgvdati.CurrentCell.RowIndex).Cells(dgvdati.CurrentCell.ColumnIndex).Value
            cerca(num)
        End If
    End Sub
End Class
'matrice quadrata quante volte si ripete sulle diagonali un numero inserityo dall'utente