Public Class Form1
    Dim N As Integer = 4
    Dim M(N - 1, N - 1) As Integer

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        creaDGV()
        crea()
    End Sub

    Sub crea()
        Randomize()
        For r = 0 To N - 1
            For c = 0 To N - 1
                M(r, c) = Int(Rnd() * 2)
            Next
        Next
        visual()
    End Sub

    Sub visual()
        dgv.Rows.Clear()
        For r = 0 To N - 1
            dgv.Rows.Add(1)
            For c = 0 To N - 1
                dgv.Rows(r).Cells(c).Value = M(r, c)
            Next
        Next
    End Sub

    Sub creaDGV()
        For c = 0 To N - 1
            dgv.Columns.Add(c, "col" & c)
            dgv.Columns(c).Width = 40
        Next
        dgv.Columns(0).Width = 40
    End Sub

    Function controllaOR(ByVal ind As Integer, ByVal num As Integer) As Boolean
        Dim c As Integer
        Dim continua As Boolean = True
        Do
            If M(ind, c) <> num Then
                continua = False
            End If
            c += 1
        Loop Until c > N - 1 Or Not continua
        Return continua
    End Function

    Function controllaVER(ByVal ind As Integer, ByVal num As Integer) As Boolean
        Dim r As Integer
        Dim continua As Boolean = True
        Do
            If M(r, ind) <> num Then
                continua = False
            End If
            r += 1
        Loop Until r > N - 1 Or Not continua
        Return continua
    End Function

    Function controllaOBL(ByVal num As Integer) As Boolean
        Dim i As Integer = 0
        Dim continua As Boolean = True
        Do
            If M(i, (N - 1) - i) <> num Then
                continua = False
            End If
            i += 1
        Loop Until Not continua Or i > N - 1
        Return continua
    End Function



    'Function controllaOB(ByVal num As Integer) As Boolean
    '    Dim i As Integer = 0
    '    controllaOB = True
    '    Do While controllaOB And M(i, N - 1 - i) = num And i < N
    '        i += 1
    '    Loop
    'End Function

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        crea()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim rig, col, num As Integer
        rig = dgv.CurrentCell.RowIndex
        col = dgv.CurrentCell.ColumnIndex
        If RadioButton1.Checked Or RadioButton2.Checked Then
            If RadioButton1.Checked Then
                num = RadioButton1.Text
            Else
                num = RadioButton2.Text
            End If
            If controllaOR(rig, num) And controllaVER(rig, num) Then
                MessageBox.Show("si")
            Else
                MessageBox.Show("no")
            End If
        End If
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        Dim num As Integer
        If RadioButton1.Checked Or RadioButton2.Checked Then
            If RadioButton1.Checked Then
                num = RadioButton1.Text
            Else
                num = RadioButton2.Text
            End If
            If controllaOBL(num) Then
                MessageBox.Show("si")
            Else
                MessageBox.Show("no")
            End If
        End If
    End Sub
End Class
