Public Class Form1
    Dim NR As Integer = 100
    Dim NC As Integer = 10
    Dim M(NR - 1, NC - 1) As Integer
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        carica()
    End Sub

    Sub carica()
        Randomize()
        If My.Computer.FileSystem.FileExists("numeri.csv") Then
            piglia()
            Label1.Text = "caricati dalla csv"
        Else
            For r = 0 To NR - 1
                For c = 0 To NC - 1
                    M(r, c) = Int(Rnd() * 90 + 1)
                Next
            Next
            Label1.Text = "caricati nuovi e casuali"
        End If
        visua()
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
        FileOpen(1, "numeri.csv", OpenMode.Output)
        For r = 0 To NR - 1
            str = ""
            For c = 0 To NC - 1
                str &= M(r, c) & ";"
            Next
            PrintLine(1, str)
        Next
        FileClose(1)
    End Sub

    Sub cancella()
        dgvdati.Columns.Clear()
        dgvdati.Rows.Clear()
        For r = 0 To NR - 1
            For c = 0 To NC - 1
                M(r, c) = 0
            Next
        Next
    End Sub

    Sub piglia()
        Dim r, c As Integer
        Dim s() As String
        FileOpen(1, "numeri.csv", OpenMode.Input)
        Do While Not EOF(1)
            s = Split(LineInput(1), ";")
            For c = 0 To NC - 1
                M(r, c) = s(c)
            Next
            r += 1
        Loop
        FileClose(1)
        visua()
    End Sub

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        salva()
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        cancella()
    End Sub

    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        piglia()
    End Sub
End Class
'con numeri casuali tra 1 e 90 
'visualizzare la matrice in una dgv
'salvare la matrice un file csv
'dopo aver svuotato la dgv e la matrice leggeere il file csv, caricare la matrice e visualizzarla nella dgv
'