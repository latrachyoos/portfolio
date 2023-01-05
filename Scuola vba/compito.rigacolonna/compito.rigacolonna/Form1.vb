Public Class Form1
    Const NR As Integer = 5
    Const NC As Integer = 4
    Dim x(NR - 1, NC - 1) As Integer

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        riempi()
        formatta()
    End Sub

    Sub riempi()
        Randomize()
        For r = 0 To NR - 1
            For c = 0 To NC - 1
                x(r, c) = Int(Rnd() * 1) + 1
            Next
        Next
    End Sub

    Sub formatta()
        dgvdati.Columns.Clear()
        dgvdati.Rows.Clear()
        For c = 0 To NC - 1
            dgvdati.Columns.Add("col", c)
            dgvdati.Columns(c).Width = 40
        Next
        visua()
    End Sub

    Sub visua()
        For r = 0 To NR - 1
            dgvdati.Rows.Add()
            For c = 0 To NC - 1
                dgvdati.Rows(r).Cells(c).Value = x(r, c)
            Next
        Next
    End Sub

    Private Sub dgvdati_CellContentClick(sender As System.Object, e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgvdati.CellContentClick
        Dim indR, indC As Integer
        indR = dgvdati.CurrentCell.RowIndex
        indC = dgvdati.CurrentCell.ColumnIndex
        MessageBox.Show("riga " & rispostaR(indR))
        MessageBox.Show("colonna " & rispostaR(indC))
    End Sub

    Function rispostaR(ByVal ind As Integer) As String
        Dim cont As Boolean = True
        Dim i As Integer = 1
        Do While cont And i < NC
            If x(ind, 0) <> x(ind, i) Then
                cont = False
            End If
        Loop
        If cont Then
            rispostaR = "si"
        Else
            rispostaR = "no"
        End If
    End Function

    Function rispostaC(ByVal ind As Integer) As String
        Dim cont As Boolean = True
        Dim i As Integer = 1
        Do While cont And i < NC
            If x(0, ind) <> x(i, ind) Then
                cont = False
            End If
        Loop
        If cont Then
            rispostaC = "si"
        Else
            rispostaC = "no"
        End If
    End Function
End Class
