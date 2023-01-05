Imports System.Data.OleDb

Public Class Form1
    Dim strconnessione As String = "provider=microsoft.jet.oledb.4.0; data source=nw.mdb"
    Dim nmax As Integer = 100
    Dim v(nmax - 1) As String
    Dim n As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim query As String

        Try
            connessione.ConnectionString = strconnessione
            connessione.Open()
            command.Connection = connessione
            query = "select distinct nazione from clienti"
            command.CommandText = query
            mreader = command.ExecuteReader
            Do While mreader.Read
                cmbnazioni.Items.Add(mreader("nazione"))
            Loop
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
        Try
            connessione.Close()
        Catch ex As Exception

        End Try
    End Sub
    Sub uptadedgv(ByVal nazione As String)
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim query As String
        Dim r As Integer
        Try
            connessione.ConnectionString = strconnessione
            connessione.Open()
            command.Connection = connessione
            query = "select NomeSocieta, idcliente from clienti where nazione = '" & nazione & "'"
            command.CommandText = query
            mreader = command.ExecuteReader
            dgv.Rows.Clear()
            Do While mreader.Read
                dgv.Rows.Add()
                dgv.Rows(r).Cells("IDcliente").Value = mreader("IDcliente")
                dgv.Rows(r).Cells("clienti").Value = mreader("NomeSocieta")
                r += 1
            Loop
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
        Try
            connessione.Close()
        Catch ex As Exception
        End Try

    End Sub
    Private Sub cmbnazioni_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmbnazioni.SelectedIndexChanged
        Dim nazione As String = cmbnazioni.SelectedItem
        uptadedgv(nazione)
    End Sub
    Private Sub dgv_CellContentClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgv.CellContentClick
        txtid.Text = "ID: " & dgv.CurrentRow.Cells("IDcliente").Value
        txtnome.Text = dgv.CurrentRow.Cells("clienti").Value
        btnmodifica.Enabled = True
        txtnome.Enabled = True
    End Sub

    Private Sub btnmodifica_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnmodifica.Click
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        If Trim(txtnome.Text) <> "" And Trim(txtnome.Text) <> "CLIENTE" Then
            If txtnome.Text <> dgv.CurrentRow.Cells("clienti").Value Then
                Dim query, id, nome As String
                nome = Trim(txtnome.Text.Replace("'", "'''"))
                id = txtid.Text.Replace("ID: ", "")
                Try
                    connessione.ConnectionString = strconnessione
                    connessione.Open()
                    command.Connection = connessione
                    query = "update clienti set nomesocieta ='" & txtnome.Text & "' where idcliente = '" & id & "'"
                    command.CommandText = query
                    command.ExecuteNonQuery()
                    connessione.Close()
                    uptadedgv(cmbnazioni.SelectedItem)
                    btnmodifica.Enabled = False
                    txtnome.Enabled = False
                    txtid.Text = "ID: "
                    txtnome.Text = "CLIENTE"
                    btnmodifica.BackColor = Color.LightGreen
                    MsgBox("Modificato correttamente")
                    btnmodifica.BackColor = Color.Transparent
                Catch ex As Exception
                    MsgBox(ex.Message)
                End Try
            Else
                btnmodifica.BackColor = Color.LightGoldenrodYellow
                MsgBox("inserisci na modifica diversa dal nome corrente")
                btnmodifica.BackColor = Color.Transparent
            End If
            Try
                connessione.Close()
            Catch ex As Exception
            End Try
        End If
    End Sub
End Class
