Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    End Sub

    Structure stcAtleti
        Dim cogn As String
        Dim nome As String
        Dim temp As Integer
    End Structure
    Dim Atl As stcAtleti
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click

        If Trim(TextBox1.Text) <> "" And Trim(TextBox2.Text) <> "" And IsNumeric(TextBox3.Text) Then
            Atl.cogn = TextBox1.Text
            Atl.nome = TextBox2.Text
            Atl.temp = TextBox3.Text
            aggiungi()
        End If
    End Sub

    Sub aggiungi()
        Dim N As Integer
        N = dgv.Rows.Count
        dgv.Rows.Add()
        dgv.Rows(N).Cells("Cognome").Value = atl.cogn
        dgv.Rows(N).Cells("Nome").Value = atl.nome
        dgv.Rows(N).Cells("Tempo").Value = atl.temp
    End Sub
End Class
