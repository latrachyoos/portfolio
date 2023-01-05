Public Class Form1
    Structure stcAtleta
        <VBFixedString(20)> Dim Cognome As String
        <VBFixedString(20)> Dim Nome As String
        Dim Tempo As Integer
    End Structure

    Dim Lrec As Integer
    Dim Nmax As Integer = 50
    Dim Atleta(Nmax - 1) As stcAtleta
    Dim N As Integer
    Dim file As String = "dati.rnd"
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        Dim A As stcAtleta
        Lrec = Len(A)
        scarica()
        visua()
    End Sub

    Sub visua()
        dgv.Rows.Clear()
        For i = 0 To N - 1
            dgv.Rows.Add()
            dgv.Rows(i).Cells("cognome").Value = Atleta(i).Cognome
            dgv.Rows(i).Cells("nome").Value = Atleta(i).Nome
            dgv.Rows(i).Cells("tempo").Value = Atleta(i).Tempo
        Next

    End Sub

    Sub scarica()
        FileOpen(1, file, OpenMode.Random, , , Lrec)
        N = LOF(1) \ Lrec
        For i = 0 To N - 1
            FileGet(1, Atleta(i), i + 1)
        Next
        FileClose()
    End Sub

    Sub carica()
        FileOpen(1, file, OpenMode.Random, , , Lrec)
        For i = 0 To N - 1
            FilePut(1, Atleta(i), i + 1)
        Next
        FileClose()
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        carica()
        Timer1.Start()
        Button2.BackColor = Color.Pink
    End Sub

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        If Trim(TextBox1.Text) <> "" And Trim(TextBox2.Text) <> "" And IsNumeric(TextBox3.Text) Then
            add()
            TextBox1.Clear()
            TextBox2.Clear()
            TextBox3.Clear()
        End If
        Timer1.Start()
        Button1.BackColor = Color.LightGreen
    End Sub

    Sub add()
        Atleta(N).Cognome = TextBox1.Text
        Atleta(N).Nome = TextBox2.Text
        Atleta(N).Tempo = TextBox3.Text
        N += 1
        visua()
    End Sub

    Private Sub dgv_CellContentClick(sender As System.Object, e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgv.Cellclick
        'dgv.Rows(dgv.CurrentCell.RowIndex).DefaultCellStyle.BackColor = Color.CadetBlue
        'dgv.Columns(dgv.CurrentCell.ColumnIndex).DefaultCellStyle.BackColor = Color.CadetBlue
        dgv.DefaultCellStyle.BackColor = Color.AliceBlue
    End Sub

    Dim num As Integer = 0
    Private Sub Timer1_Tick(sender As System.Object, e As System.EventArgs) Handles Timer1.Tick
        num += 1
        If num > 1 Then
            Timer1.Stop()
            Button1.BackColor = Color.LightGray
            Button2.BackColor = Color.LightGray
        End If
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnCambioposizione.Click
        Dim pos As New Point(Rnd() * 1000, Rnd() * 300)
        Dim col As Color = Color.FromArgb((Rnd() * 255) + 1, (Rnd() * 255) + 1, (Rnd() * 255) + 1)
        Dim siz As New Size((Rnd() * 100) + 10, (Rnd() * 100) + 10)
        btnCambioposizione.Location = pos
        btnCambioposizione.BackColor = col
        btnCambioposizione.Size = siz

    End Sub
End Class
