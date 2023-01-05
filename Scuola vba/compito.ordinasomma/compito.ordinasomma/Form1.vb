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
                x(r, c) = Int(Rnd() * NR) + 1
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

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim v(NR * NC - 1) As Integer
        scarica(v, x)
        ordine(v, x)
        carica(v, x)
        visua()
    End Sub

    Sub scarica(ByRef v() As Integer, ByRef x(,) As Integer)
        Dim i As Integer
        For r = 0 To NR - 1
            For c = 0 To NC - 1
                v(i) = x(r, c)
                i += 1
            Next
        Next
    End Sub

    Sub ordine(ByRef v() As Integer, ByRef x(,) As Integer)
        Dim con As Boolean = True
        Dim p As Integer
        Do While con
            con = False
            For i = 0 To v.GetUpperBound(0) - 1 - p
                If v(i) > v(i + 1) Then
                    con = True
                    change(v(i), v(i + 1))
                End If
            Next
            p += 1
        Loop
    End Sub

    Sub change(ByRef A As Integer, ByRef B As Integer)
        Dim C As Integer = A
        A = B
        B = C
    End Sub

    Sub carica(ByRef v() As Integer, ByRef x(,) As Integer)
        Dim i As Integer
        For r = 0 To NR - 1
            For c = 0 To NC - 1
                x(r, c) = v(i)
                i += 1
            Next
        Next
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Dim ind As Integer = dgvdati.CurrentRow.Index
        If ind > -1 Then
            MessageBox.Show(somma(ind, x))
        Else
            MessageBox.Show("no")
        End If
    End Sub

    Function somma(ByVal ind As Integer, ByRef x(,) As Integer) As Integer
        Dim s, r, c As Integer
        r = ind
        Do
            s += x(r, c)
            r += 1
            c += 1
        Loop Until r > NR - 1 Or c > NC - 1
        Return s
    End Function
End Class
