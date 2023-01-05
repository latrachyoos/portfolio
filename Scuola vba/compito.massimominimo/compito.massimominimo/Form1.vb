Public Class Form1
    Const NR As Integer = 15
    Const NC As Integer = 14
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
        dgvdati.Rows.Clear()
        For r = 0 To NR - 1
            dgvdati.Rows.Add()
            For c = 0 To NC - 1
                dgvdati.Rows(r).Cells(c).Value = x(r, c)
            Next
        Next
    End Sub

    Private Sub btnmax_Click(sender As System.Object, e As System.EventArgs) Handles btnmax.Click
        Dim ind As Integer = dgvdati.CurrentCell.RowIndex
        If ind >= 0 Then
            MessageBox.Show(massimo(ind, x))
        End If

    End Sub

    Private Sub btnmin_Click(sender As System.Object, e As System.EventArgs) Handles btnmin.Click
        Dim ind As Integer = dgvdati.CurrentCell.RowIndex
        If ind >= 0 Then
            minore(ind, x)
        End If
    End Sub

    Private Sub btnord_Click(sender As System.Object, e As System.EventArgs) Handles btnord.Click
        Dim ind As Integer = dgvdati.CurrentCell.RowIndex
        If ind >= 0 Then
            ordina(ind, x)
        End If
    End Sub

    Function massimo(ByVal ind As Integer, ByRef x(,) As Integer) As Integer
        Dim max As Integer = x(ind, 0)
        For c = 1 To x.GetUpperBound(1)
            If x(ind, c) > max Then
                max = x(ind, c)
            End If
        Next
        Return max
    End Function

    Sub minore(ByVal ind As Integer, ByRef x(,) As Integer)
        Dim min As Integer = x(ind, 0)
        Dim i As Integer
        For c = 1 To x.GetUpperBound(1)
            If min > x(ind, c) Then
                min = x(ind, c)
                i = c
            End If
        Next
        If i <> 0 Then
            change(x(ind, 0), x(ind, i))
        End If
        visua()
    End Sub

    Sub change(ByRef a As Integer, ByRef b As Integer)
        Dim c As Integer = a
        a = b
        b = c
    End Sub

    Sub ordina(ByVal ind As Integer, ByRef x(,) As Integer)
        Dim ferma As Boolean = False
        Dim pos As Integer
        Do While Not ferma
            ferma = True
            For c = 0 To x.GetUpperBound(1) - 1 - pos
                If x(ind, c) < x(ind, c + 1) Then
                    change(x(ind, c), x(ind, c + 1))
                    ferma = False
                End If
            Next
            pos += 1
        Loop
        visua()
    End Sub
End Class
