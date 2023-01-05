Public Class Form1
    Dim NR As Integer = 10
    Dim NC As Integer = 3
    Dim M(NR - 1, NC - 1) As String
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load

    End Sub

    Sub visua()
        dgvdati.Columns.Clear()
        dgvdati.Rows.Clear()
        dgvdati.ColumnCount = NC
        dgvdati.Rows.Add(NR - 1)
        For r = 0 To NR - 1
            For c = 0 To NC - 1
                dgvdati.Rows(r).Cells(c).Value = M(r, c)
            Next
        Next
    End Sub

    Sub salva()
        Dim str As String
        FileOpen(1, "persone.csv", OpenMode.Append)
        For r = 0 To NR - 1
            str = ""
            For c = 0 To NC - 1
                str &= M(r, c) & ";"
            Next
            PrintLine(1, str)
        Next
        FileClose(1)
    End Sub

    Sub piglia()
        Dim r, c As Integer
        Dim s() As String
        FileOpen(1, "persone.csv", OpenMode.Input)
        Do While Not EOF(1)
            s = Split(LineInput(1), ";")
            M(r, c) = s(c)
            c += 1
            If c = 3 Then
                c = 0
                r = 1
            End If
        Loop
        FileClose(1)
        visua()
    End Sub

    Private Sub Button1_Click_1(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        If Trim(TextBox1.Text) <> "" And Trim(TextBox2.Text) <> "" And Trim(IsNumeric(TextBox3.Text)) Then
            salva()
        End If
    End Sub



    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        piglia()
    End Sub

End Class