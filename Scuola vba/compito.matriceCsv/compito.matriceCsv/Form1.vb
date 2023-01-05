Public Class Form1
    Const NR As Integer = 50
    Const NC As Integer = 40
    Dim x(NR - 1, NC - 1) As Integer

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        riempi()
        formatta()
    End Sub

    Sub riempi()
        Randomize()
        For r = 0 To NR - 1
            For c = 0 To NC - 1
                x(r, c) = Int(Rnd() * NC * NR) + 1
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

    Dim file As String = "dati.csv"
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim list As String
        FileOpen(1, file, OpenMode.Output)
        For r = 0 To NR - 1
            list = ""
            For c = 0 To NC - 1
                If c > 0 Then
                    list &= ";"
                End If
                list &= x(r, c)
            Next
            PrintLine(1, list)
        Next
        FileClose(1)
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Dim r As Integer
        Dim s() As String
        FileOpen(1, file, OpenMode.Input)
        Do While Not EOF(1)
            s = Split(LineInput(1), ";")
            For c = 0 To NC - 1
                x(r, c) = s(c)
            Next
            r += 1
        Loop
        FileClose(1)
        formatta()
    End Sub

    Private Sub dgvdati_CellContentClick(sender As System.Object, e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgvdati.CellContentClick
        Dim ind As Integer = dgvdati.CurrentCell.RowIndex()
        Dim tot As Double = x(ind, 0)
        For c = 0 To NC - 1
            tot *= x(ind, c)
        Next
        MessageBox.Show(tot)
    End Sub
End Class
